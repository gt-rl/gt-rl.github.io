"""Get all camera-ready PDFs."""

import io
import openreview
import os
import requests

from dotenv import load_dotenv

load_dotenv()


def download(url, number, prefix):
    """Download data and store it, associated to a paper."""
    data = requests.get(pdf_url)
    content_type = data.headers.get("content-type")

    print(content_type)

    if content_type == "application/pdf":
        with open(f"/tmp/{prefix}{number:02d}.pdf", "wb") as f:
            f.write(data.content)


if __name__ == "__main__":
    client = openreview.api.OpenReviewClient(
        baseurl="https://api.openreview.net",
        username=os.getenv("OPENREVIEW_USER"),
        password=os.getenv("OPENREVIEW_PASSWORD"),
    )

    all_notes = list(
        client.get_all_notes(
            invitation="SampTA/2023/Conference/-/Blind_Submission",
            details="directReplies,original",
        )
    )

    accepted_papers = []
    decisions = []

    for note in all_notes:
        decisions = decisions + [
            reply
            for reply in note.details["directReplies"]
            if reply["invitation"].endswith("Decision")
        ]

        decision = decisions[-1]["content"]["decision"]

        if decision == "Accept (Paper)":
            number = note.number
            pdf = note.content["pdf"]
            supp = note.content.get("supplementary_materials", None)

            pdf_url = f"https://openreview.net{pdf}"
            supp_url = f"https://openreview.net{supp}"

            download(pdf_url, number, "Main_")

            if supp is not None:
                download(supp_url, number, "Supp_")
