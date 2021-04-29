"""Download posters of accepted papers."""

import filetype
import openreview
import os
import requests

from slugify import slugify
from tqdm import tqdm


if __name__ == '__main__':

    # TODO: could make this configurable?
    os.makedirs('data', exist_ok=True)
    os.makedirs('data/posters', exist_ok=True)

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

    # Sort by title to get a consistent ordering.
    accepted_notes = sorted(
        accepted_notes,
        key=lambda x: x.content['title'].lower()
    )

    for note in tqdm(accepted_notes, desc='Papers'):

        title = note.content['title'].strip()
        authors = note.content['authors']

        forum = note.forum
        pdf_url = f'https://openreview.net/pdf?id={forum}'
        forum_url = f'https://openreview.net/forum?id={forum}'

        if 'Poster' not in note.content:
            continue

        poster_url = \
            f'https://openreview.net/attachment?id={forum}&name=Poster'

        poster_request = requests.get(poster_url)
        if poster_request.status_code == requests.codes.ok:

            ft = filetype.guess(poster_request.content)
            ext = ft.extension

            filename = os.path.join(
                'data', 'posters', slugify(title) + f'.{ext}'
            )

            with open(filename, 'wb') as f:
                f.write(poster_request.content)
