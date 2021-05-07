"""Get author information for workshop papers."""

import openreview
import os

from dotenv import load_dotenv
from openreview.openreview import OpenReviewException

load_dotenv()


def get_full_name(profile):
    """Get full name from profile."""
    for name in profile.content['names']:
        if 'preferred' not in name.keys() or name['preferred']:
            if name['middle']:
                return ' '.join([
                    name['first'], name['middle'], name['last']
                ])
            else:
                return ' '.join([
                    name['first'], name['last']
                ])

    return ''


if __name__ == '__main__':

    client = openreview.Client(
        baseurl='https://api.openreview.net',
        username=os.getenv('OPENREVIEW_USER'),
        password=os.getenv('OPENREVIEW_PASSWORD')
    )

    accepted_papers = client.get_notes(
        content={'venueid': 'ICLR.cc/2021/Workshop/GTRL'}
    )

    notes = client.get_notes(
        content={'venueid': 'ICLR.cc/2021/Workshop/GTRL'}
    )

    authors = set()

    for note in notes:
        author_ids = note.content['authorids']

        for author_id in author_ids:
            if '@' in author_id:
                try:
                    profile = client.get_profile(author_id)
                except OpenReviewException:
                    authors.add(author_id)
                    continue
            else:
                profile = client.search_profiles(ids=[author_id])[0]
            authors.add(get_full_name(profile))

    print(sorted(authors))
