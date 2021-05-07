"""Create wordclout from submissions."""

import io
import openreview
import requests

import matplotlib.pyplot as plt

from tqdm import tqdm

from pdfminer.high_level import extract_text

from wordcloud import WordCloud, STOPWORDS

if __name__ == '__main__':

    client = openreview.Client(baseurl='https://api.openreview.net')

    all_decision_notes = list(openreview.tools.iterget_notes(
        client,
        invitation='ICLR.cc/2021/Workshop/GTRL/Paper.*/-/Decision',
    ))

    # IDs of accepted papers for querying their posters later on.
    papers = []

    for note in all_decision_notes:
        if 'Accept' in note.content['decision']:
            papers.append(note.forum)

    # Get all blind notes to find the *original* forum ID for
    # a submission, so that we can generate proper URLs later
    # on.
    blind_notes = {
        note.forum: note for note in openreview.tools.iterget_notes(
            client,
            invitation='ICLR.cc/2021/Workshop/GTRL/-/Blind_Submission',
            details='original',
        )
    }

    accepted_notes = [
        blind_notes[forum] for forum in blind_notes.keys()
        if forum in papers
    ]

    all_text = ""

    for note in tqdm(accepted_notes, desc='Paper'):
        pdf_url = f'https://openreview.net/pdf?id={note.id}'
        data = requests.get(pdf_url)
        content = io.BytesIO(data.content)
        text = extract_text(content)

        all_text += text

    stopwords = set(STOPWORDS)
    stopwords.add('cid')
    stopwords.update([
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'h',
        's',
        't',
        'n',
        'j',
        'figure',
        'x',
        'm',
        'h',
        'f',
        'p',
        'et',
        'al',
        'point',
        'ICLR',
        'international',
        'conference',
    ])

    wc = WordCloud(
        width=1200,
        height=600,
        max_words=500,
        background_color='white',
        color_func=lambda *args, **kwargs: 'black',
        stopwords=stopwords,
    )

    wc.generate(all_text)
    wc.to_file('word_cloud.png')

    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()
