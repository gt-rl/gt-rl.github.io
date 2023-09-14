"""Get all camera-ready PDFs."""

import openreview
import os
import requests

from dotenv import load_dotenv

load_dotenv()


def download(prefix, client, note_id, number, data_type, ext):
    """Download data and store it, associated to a paper."""
    data = client.get_attachment(note_id, data_type)

    print(ext)

    with open(f"/tmp/{prefix}{number:02d}{ext}", "wb") as f:
        f.write(data)


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
            download("SampTA_Main_", client, note.id, number, "pdf", ".pdf")

            # It is not enough to check for "is None" here, since some
            # materials are stored with an empty string.
            if supp := note.content.get("supplementary_materials"):
                download(
                    "SampTA_Supp_",
                    client,
                    note.id,
                    number,
                    "supplementary_materials",
                    os.path.splitext(supp)[1],
                )
