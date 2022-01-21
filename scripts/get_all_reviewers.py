"""Get reviewer information for workshop papers."""

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

    #notes = client.get_notes(
    #    content={'venueid': 'ICLR.cc/2021/Workshop/GTRL'}
    #)

    #print(notes)

    reviewers = []
    addresses = []

    for member in client.get_group(
            id='ICLR.cc/2021/Workshop/GTRL/Reviewers').members:
        try:
            if '@' in member:
                addresses.append(member)
            else:
                profile = client.search_profiles(ids=[member])[0]
        except OpenReviewException:
            pass

        reviewers.append(profile)

    for profile in reviewers:
        email = profile.content.get(
            'preferredEmail', profile.content['emails'][0]
        )

        addresses.append(email)

    addressses = set(addresses)

    for email in addressses:
        print(email)
