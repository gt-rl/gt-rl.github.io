"""Get author information for workshop papers."""

from dotenv import load_dotenv

import openreview
import os

from openreview.openreview import OpenReviewException


load_dotenv()


if __name__ == "__main__":

    client = openreview.api.OpenReviewClient(
        baseurl="https://api2.openreview.net",
        username=os.getenv("OPENREVIEW_USER"),
        password=os.getenv("OPENREVIEW_PASSWORD"),
    )

    #notes = client.get_all_notes(
    #    invitation="SampTA/2023/Conference/-/Blind_Submission",
    #    details="directReplies",
    #)

    #print("Received", len(notes), "notes")

    #n_rejected = 0

    #rejected_papers = []

    #for note in notes:
    #    rejected = False

    #    for reply in note.details["directReplies"]:
    #        if reply["invitation"].endswith("Decision"):
    #            if reply["content"]["decision"] == "Reject":
    #                rejected = True
    #                n_rejected += 1
    #                break

    #    if rejected:
    #        rejected_papers.append(note.original)

    notes = client.get_all_notes(
        content={'venueid':'ICML.cc/2023/Workshop/TAGML/Submission'}, sort='number:asc')
        #invitation="ICML.cc/2023/Workshop/TAGML/-/Submission",

    for note in notes:
        #if note.forum not in rejected_papers:
        #    continue
        #else:
        #    n_found_rejected += 1

        author_ids = note.content["authorids"]["value"]
        #print(note.content["title"])

        for author_id in author_ids:
            if "@" in author_id:
                print(author_id)
            elif author_id.startswith("~"):
                profile = client.search_profiles(ids=[author_id])[0]
                email = profile.content.get(
                    "preferredEmail", profile.content["emails"][0]
                )
                print(email)

    #assert n_rejected == n_found_rejected
