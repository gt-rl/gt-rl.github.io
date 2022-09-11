"""Download titles of accepted papers."""

from dotenv import load_dotenv
from wordcloud import WordCloud, STOPWORDS

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

    for submission in submissions:
        title = submission.content["title"]
        abstract = submission.content["abstract"]
        url = f"https://openreview.net/forum?id={submission.forum}"

        words = abstract.split()

        if len(words) < 10:
            print(f"{title}: {len(words)} word(s) ({url})")
    
        text += title #+ " " + abstract

    stopwords = set(STOPWORDS)

    wc = WordCloud(
        width=1200,
        height=600,
        max_words=500,
        background_color='white',
        color_func=lambda *args, **kwargs: 'black',
        stopwords=stopwords,
    )

    wc.generate(text)
    wc.to_file("word_cloud.png")
