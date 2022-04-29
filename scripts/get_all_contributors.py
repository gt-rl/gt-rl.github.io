"""Get author information for workshop papers."""

import collections
import locale
import openreview
import os

from dotenv import load_dotenv

from functools import cmp_to_key

from openreview.openreview import OpenReviewException

from requests.exceptions import HTTPError

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

    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    client = openreview.Client(
        baseurl='https://api.openreview.net',
        username=os.getenv('OPENREVIEW_USER'),
        password=os.getenv('OPENREVIEW_PASSWORD')
    )

    notes = client.get_notes(
        content={'venueid': 'ICLR.cc/2022/Workshop/GTRL'}
    )

    all_profiles = []
    contributors = set()

    for member in client.get_group(
            id='ICLR.cc/2022/Workshop/GTRL/Area_Chairs').members:
        all_profiles.append(client.get_profile(member))

    for note in notes:
        author_ids = note.content['authorids']

        for author_id in author_ids:
            if '@' in author_id:
                try:
                    profile = client.get_profile(author_id)
                except OpenReviewException:
                    contributors.add(author_id)
                    continue
            else:
                profile = client.search_profiles(ids=[author_id])[0]
                all_profiles.append(profile)

    for profile in all_profiles:
        contributors.add(get_full_name(profile))

    reviewers = collections.defaultdict(list)

    for review in openreview.tools.iterget_notes(
        client,
        invitation='ICLR.cc/2022/Workshop/GTRL/Paper.*/-/Official_Review'
    ):
        assert len(review.signatures) == 1

        try:
            members = client.get_group(id=review.signatures[0]).members
        except OpenReviewException:
            continue
        except HTTPError:
            continue

        # We only expect a single reviewer here.
        assert len(members) == 1

        profile = client.get_profile(members[0])
        name = get_full_name(profile)

        reviewers[name].append(review.content['review'])

    contributors.update(reviewers.keys())

    for contributor in sorted(contributors, key=cmp_to_key(locale.strcoll)):
        print(contributor)
