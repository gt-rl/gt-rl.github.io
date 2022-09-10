"""Download titles of accepted papers."""

from dotenv import load_dotenv

import openreview
import os

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

    for submission in submissions:
        title = submission.content["title"]
        abstract = submission.content["abstract"]
        url = f"https://openreview.net/forum?id={submission.forum}"

        words = abstract.split()

        if len(words) < 10:
            print(f"{title}: {len(words)} word(s) ({url})")
