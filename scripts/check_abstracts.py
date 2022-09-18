"""Check abstracts for text overlap."""

from dotenv import load_dotenv

import matplotlib.pyplot as plt
import seaborn as sns

import itertools
import openreview
import spacy
import os

load_dotenv()


if __name__ == "__main__":
    nlp = spacy.load("en_core_web_md")

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

    data = []

    for submission in submissions:
        title = submission.content["title"]
        abstract = submission.content["abstract"]
        url = f"https://openreview.net/forum?id={submission.forum}"

        data.append((title, abstract, url))

    similarities = []

    for sub1, sub2 in itertools.combinations(data, r=2):
        title1, abstract1, url1 = sub1
        title2, abstract2, url2 = sub2

        abstract1 = nlp(abstract1)
        abstract2 = nlp(abstract2)

        similarity = abstract1.similarity(abstract2)

        if similarity >= 0.99:
            print(title1, "<->", title2)

        similarities.append(similarity)

    sns.histplot(data=similarities)
    plt.show()
