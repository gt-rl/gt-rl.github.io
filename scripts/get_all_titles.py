"""Download titles of accepted papers."""

import openreview


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

    # Sort by title to get a consistent ordering.
    accepted_notes = sorted(
        accepted_notes,
        key=lambda x: x.content['title'].lower()
    )

    for note in accepted_notes:

        title = note.content['title'].strip()
        forum = note.forum
        pdf_url = f'https://openreview.net/pdf?id={forum}'
        print(f'{title}\t{pdf_url}')
