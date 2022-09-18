"""Check whether paper has a PDF."""

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

    text = ""

    for index, submission in enumerate(submissions):
        content = submission.content
        url = f"https://openreview.net/forum?id={submission.forum}"

        if not "PDF_file" in content:
            print(f"{index},{content['title']},{url}")
