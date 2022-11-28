"""Get reviewer information for papers."""

import locale
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

    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    client = openreview.Client(
        baseurl='https://api.openreview.net',
        username=os.getenv('OPENREVIEW_USER'),
        password=os.getenv('OPENREVIEW_PASSWORD')
    )

    reviewers = []
    addresses = []

    for id in ['ICLR.cc/2021/Workshop/GTRL/Reviewers',
               'NeurIPS.cc/2020/Workshop/TDA_and_Beyond/Reviewers']:

        for member in client.get_group(id=id).members:
            try:
                if '@' in member:
                    addresses.append(member)

                    # Prevent duplicate profiles
                    continue
                else:
                    profile = client.search_profiles(ids=[member])[0]
            except OpenReviewException:
                pass

            reviewers.append(profile)

    for profile in reviewers:
        name = get_full_name(profile)

        email = profile.content.get(
            'preferredEmail', profile.content['emails'][0]
        )

        addresses.append(f'{email},{name}')

    addressses = set(addresses)

    for email in sorted(addressses):
        print(email)
