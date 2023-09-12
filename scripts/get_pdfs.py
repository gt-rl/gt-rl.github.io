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

    raise "heck"

    # Get all blind notes to find the *original* forum ID for
    # a submission, so that we can generate proper URLs later
    # on.
    blind_notes = {
        note.forum: note
        for note in openreview.tools.iterget_notes(
            client,
            invitation="ICLR.cc/2021/Workshop/GTRL/-/Revisoin",
            details="original",
        )
    }

    accepted_notes = [
        blind_notes[forum] for forum in blind_notes.keys() if forum in papers
    ]

    all_text = ""

    for note in tqdm(accepted_notes, desc="Paper"):
        pdf_url = f"https://openreview.net/pdf?id={note.id}"
        data = requests.get(pdf_url)
        content = io.BytesIO(data.content)
        text = extract_text(content)

        all_text += text

    stopwords = set(STOPWORDS)
    stopwords.add("cid")
    stopwords.update(
        [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "s",
            "t",
            "n",
            "j",
            "figure",
            "x",
            "m",
            "h",
            "f",
            "p",
            "et",
            "al",
            "point",
            "ICLR",
            "international",
            "conference",
        ]
    )

    wc = WordCloud(
        width=1200,
        height=600,
        max_words=500,
        background_color="white",
        color_func=lambda *args, **kwargs: "black",
        stopwords=stopwords,
    )

    wc.generate(all_text)
    wc.to_file("word_cloud.png")

    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()
