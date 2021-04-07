"""Get author information for workshop papers."""

import openreview

from openreview.openreview import OpenReviewException


if __name__ == '__main__':

    client = openreview.Client(
        baseurl='https://api.openreview.net',
    )

    notes = list(
        openreview.tools.iterget_notes(
            client,
            invitation='ICLR.cc/2021/Workshop/GTRL/-/Blind_Submission',
            details='original',
        )
    )

    for note in notes:
        author_ids = note.content['authorids']

        for author_id in author_ids:
            try:
                profile_info = openreview.tools.get_profile_info(
                    client.get_profile(author_id)
                )

                print(profile_info)
            except OpenReviewException:
                print(author_id)
                pass
