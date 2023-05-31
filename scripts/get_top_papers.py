from dotenv import load_dotenv

import pandas as pd

import openreview
import os
import random
import sys
import titlecase


load_dotenv()


def parse_author_ids(ids):
    return ids.split("|")


if __name__ == "__main__":
    client = openreview.api.OpenReviewClient(
        baseurl="https://api.openreview.net",
        username=os.getenv("OPENREVIEW_USER"),
        password=os.getenv("OPENREVIEW_PASSWORD"),
    )

    filename = sys.argv[1]

    top_k = 20

    df = pd.read_csv(filename)
    df.set_index("number", inplace=True)

    decision = "Accept (Paper)"
    df = df[df.decision == decision]
    df = df.sort_values(by="average rating", ascending=False)

    emails = []
    titles = []

    for index, row in df.head(n=top_k).iterrows():
        ids = row["authorids"]
        ids = parse_author_ids(ids)

        titles.append(titlecase.titlecase(row["title"]))

        for author_id in ids:
            if "@" in author_id:
                emails.append(author_id)
            elif author_id.startswith("~"):
                profile = client.search_profiles(ids=[author_id])[0]
                email = profile.content.get(
                    "preferredEmail", profile.content["emails"][0]
                )
                emails.append(email)

    emails = set(emails)
    for email in emails:
        print(email)

    random.shuffle(titles)
    for title in titles:
        print(title)
