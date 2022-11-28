"""Get statistics about submissions."""

from collections import Counter
from dotenv import load_dotenv

import openreview
import os
import sys

load_dotenv()


if __name__ == "__main__":
    client = openreview.Client(
        baseurl="https://api.openreview.net",
        username=os.getenv("OPENREVIEW_USER"),
        password=os.getenv("OPENREVIEW_PASSWORD"),
    )

    submissions = client.get_notes(
        invitation="logconference.io/LOG/2022/Conference/-/Submission",
        details="original",
    )

    all_subs = Counter()
    id_to_type = {}

    for submission in submissions:
        sub_type = submission.content["Type of submission"]
        all_subs[sub_type] += 1

        id_to_type[submission.forum] = sub_type
        id_to_type[submission.id] = sub_type

    print(all_subs.most_common())

    # Despite its name, this invitation contains all of the active
    # submission of the conference, i.e. all the submissions that have
    # not been desk-rejected or withdrawn.
    submissions = client.get_notes(
        invitation="logconference.io/LOG/2022/Conference/-/Blind_Submission",
        details="original",
    )

    cur_subs = Counter()

    for submission in submissions:
        sub_type = submission.content["Type of submission"]
        cur_subs[sub_type] += 1


        id_to_type[submission.id] = sub_type
        id_to_type[submission.forum] = sub_type
        id_to_type[submission.original] = sub_type

    print(cur_subs.most_common())

    # Now let's see what decisions we have available for those. This
    # will enable us to finally print a nice set of numbers.

    dec_subs = Counter()

    decision_notes = list(
        openreview.tools.iterget_notes(
            client,
            invitation="logconference.io/LOG/2022/Conference/Paper.*/Decision",
            details="original",
        )
    )

    for note in decision_notes:
        decision = note.content["decision"]
        if note.forum in id_to_type:
            dec_subs[id_to_type[note.forum] + " -- " + decision] += 1

    print(dec_subs.most_common())
