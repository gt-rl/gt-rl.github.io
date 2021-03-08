"""Assign papers to area chairs."""

import openreview
import sys


if __name__ == '__main__':

    client = openreview.Client(
        baseurl='https://api.openreview.net',
        username='bastian.rieck@bsse.ethz.ch',
        password='',
    )

    notes = list(
        openreview.tools.iterget_notes(
            client,
            invitation='ICLR.cc/2021/Workshop/GTRL/-/Blind_Submission',
            details='original',
        )
    )

    numbers = [note.number for note in notes]

    emails = [
        'mhajij@scu.edu',
        'ashukl20@asu.edu',
        'petri.giovanni@gmail.com'
    ]

    n_chairs = len(emails)

    conference = openreview.helpers.get_conference(client, 'fKfYw_pGYYG')

    for index, number in enumerate(numbers):
        if index % n_chairs == 0:
            print(number)

            conference.set_assignment(
                number=number,
                user='~Mustafa_Hajij1',
                is_area_chair=True,
            )
