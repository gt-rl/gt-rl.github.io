"""Get author information for workshop papers."""

import openreview

from openreview.openreview import OpenReviewException


if __name__ == '__main__':

    client = openreview.Client(
        baseurl='https://api.openreview.net',
        username='bastian.rieck@bsse.ethz.ch',
    )

    accepted_papers = client.get_notes(
        content={'venueid': 'ICLR.cc/2021/Workshop/GTRL'}
    )

    notes = client.get_notes(
        content={'venueid': 'ICLR.cc/2021/Workshop/GTRL'}
    )

    print('Received', len(notes), 'notes')

    for note in notes:
        author_ids = note.content['authorids']

        print(note.content['title'])

        for author_id in author_ids:
            if '@' in author_id:
                print(' ', author_id)
            else:
                profile = client.search_profiles(ids=[author_id])[0]
                email = profile.content.get(
                    'preferredEmail', profile.content['emails'][0]
                )
                print(' ', email)
