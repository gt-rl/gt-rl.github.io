import os
import re

import openreview
import pandas as pd

from dotenv import load_dotenv

load_dotenv()


def handle_venue(client, venue):
    """Handle specific venue and get all papers."""
    invitation = f"{venue}/-/Blind_Submission"

    # TODO: This should enable us to query older conferences as well but
    # it does not work for all years.
    if "conference" in venue:
        invitation = f"{venue}/-/submission"

    all_submissions = client.get_all_notes(
        invitation=invitation,
        # This is required to ensure that we can access the decisions of
        # each paper afterwards.
        details="directReplies",
    )

    print(venue)
    print("--", len(all_submissions), "submissions in total")

    id_to_submission = {note.id: note for note in all_submissions}

    all_decision_notes = []
    accepted_submissions = []

    # ICLR 2019 used meta reviews; the recommendation is akin to the
    # decision here. What a nightmare.
    if venue == "ICLR.cc/2019/Conference":
        suffix = "Meta_Review"
        decision = "recommendation"
    else:
        suffix = "Decision"
        decision = "decision"

    for note in all_submissions:
        all_decision_notes.extend(
            [
                reply
                for reply in note.details["directReplies"]
                if reply["invitation"].endswith(suffix)
                # This is necessary because at least one conference,
                # viz., ICLR 2017, encodes decisions in a field that
                # is named "acceptance" instead of "decision".
                or reply["invitation"].endswith("acceptance")
            ]
        )

        # Special handling for conferences that do not have special
        # decision notes
        if "decision" in note.content:
            decision = note.content["decision"]

            # The decision notes are of the following form:
            #
            # conferencePoster-iclr2013-workshop: workshop submission
            #
            # conferenceOral-iclr2013-conference: ditto
            # conferencePoster-iclr2013-conference: conference submission
            #
            # Since we are not interested in making a distinction
            # between orals and posters, we just accept as-is.
            if decision.endswith("conference"):
                accepted_submissions.append(note)

    print("--", len(all_decision_notes), "decision notes")

    # We use `extend` here because some conferences use direct
    # decisions in the contents of a note, which we can use in
    # order to *directly* accept a submission.
    accepted_submissions.extend(
        [
            id_to_submission[note["forum"]]
            for note in all_decision_notes
            if "Accept" in note["content"][decision]
        ]
    )

    print("--", len(accepted_submissions), "accepted submissions")

    rows = []

    for submission in accepted_submissions:
        authors = submission.content["authors"]
        key = submission.id
        title = submission.content["title"]
        abstract = submission.content["abstract"]

        # Sanitize the title. This is not done automatically, and older
        # venues of ICLR contain some junk characters.
        title = title.replace("\r", "")
        title = title.replace("\n", "")
        title = re.sub(" +", " ", title)

        # Some venues do not have submission dates. Let's use a rather
        # brittle extraction procedure instead.
        year = venue.split("/")[1]

        rows.append(
            {
                "key": key,
                "author": ";".join([author.strip() for author in authors]),
                "title": title,
                "abstract": abstract,
                "year": year,
            }
        )

    print("")
    return pd.DataFrame.from_records(rows)


if __name__ == "__main__":
    username = os.getenv("OPENREVIEW_USER")
    password = os.getenv("OPENREVIEW_PASSWORD")

    client = openreview.Client(
        baseurl="https://api.openreview.net",
        username=username,
        password=password,
    )

    venues = client.get_group(id="venues").members
    venues = [venue for venue in venues if "iclr.cc" in venue.lower()]
    venues = [venue for venue in venues if "conference" in venue.lower()]

    df = [handle_venue(client, venue) for venue in venues]

    df = pd.concat(df)
    df.to_csv("iclr.csv", index=False)
