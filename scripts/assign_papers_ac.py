"""Assign papers to area chairs."""

import os
import openreview

from dotenv import load_dotenv
load_dotenv()


if __name__ == '__main__':

    client = openreview.Client(
        baseurl='https://api.openreview.net',
        username=os.getenv('OPENREVIEW_USER'),
        password=os.getenv('OPENREVIEW_PASSWORD')
    )

    notes = list(
        openreview.tools.iterget_notes(
            client,
            invitation='ICLR.cc/2022/Workshop/GTRL/-/Blind_Submission',
            details='original',
        )
    )

    numbers = [note.number for note in notes]

    emails = [
        'mustafahajij@gmail.com',
        'ashukl20@asu.edu',
        'charu.sharma@iiit.ac.in',
    ]

    n_chairs = len(emails)

    conference = openreview.helpers.get_conference(client, '15tr0OcIj69')

    for index, number in enumerate(numbers):
        print(number, '-->', emails[index % 3])

        conference.set_assignment(
            number=number,
            user=emails[index % 3],
            is_area_chair=True,
        )
