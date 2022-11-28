"""Send e-mails to authors that allow contact."""

from dotenv import load_dotenv

import openreview
import os
import sys

load_dotenv()


if __name__ == "__main__":
    client = openreview.Client(
        baseurl="https://api.openreview.net",
        username=os.getenv("OPENREVIEW_USER"),
        password=os.getenv("OPENREVIEW_PASSWORD"),
    )

    submissions = client.get_notes(
        invitation="logconference.io/LOG/2022/Conference/-/Blind_Submission",
        details="directReplies",
    )

    author_ids = set()
    index = 0

    for submission in submissions:
        index += 1
        if "Agreement" not in submission.content:
            continue

        author_ids.update(submission.content["authorids"])

    print(f"Got {index} submissions", file=sys.stderr)

    e_mails = set([a for a in author_ids if "@" in a])

    profiles = client.search_profiles(
        ids=[a for a in author_ids if a.startswith("~")]
    )
    for profile in profiles:
        e_mails.update([profile.get_preferred_email()])

    print(f"Got {len(e_mails)} e-mail addresses", file=sys.stderr)

    with open(sys.argv[1]) as f:
        message = f.read()

    # Make sure that we don't spam too much.
    if not input("Are you sure? (y/n): ").lower().strip()[:1] == "y":
        sys.exit(1)

    client.post_message(
        subject="LoG: Survey for authors",
        recipients=sorted(e_mails),
        message=message,
        replyTo="bastian.rieck@helmholtz-muenchen.de",
    )
