"""Convert accepted papers to Markdown for website integration.""" 

import openreview
import json
import os

from tqdm import tqdm


if __name__ == '__main__':
    client = openreview.Client(baseurl='https://api.openreview.net')

    all_decision_notes = list(openreview.tools.iterget_notes(
        client,
        invitation='ICLR.cc/2021/Workshop/GTRL/Paper.*/-/Decision',
    ))

    # IDs of accepted papers and IDs of spotlights. Will be used later
    # on to populate the list of all papers.
    papers = []
    spotlights = []

    for note in all_decision_notes:
        if 'Accept' in note.content['decision']:
            papers.append(note.forum)
            if 'Spotlight' in note.content['decision']:
                spotlights.append(note.forum)

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

    for note in tqdm(accepted_notes, desc='Papers'):

        title = note.content['title'].strip()
        authors = note.content['authors']

        forum = note.forum
        pdf_url = f'https://openreview.net/pdf?id={forum}'
        forum_url = f'https://openreview.net/forum?id={forum}'

        if 'Poster' in note.content:
            poster_url = f'https://openreview.net/attachment?id={forum}&name=Poster'
        else:
            poster_url = ''

        if forum in spotlights:
            spotlight = '(Spotlight presentation)'
        else:
            spotlight = ''

        print(f'**{title}** {spotlight}<br />')
        authors = ' &bull; '.join(authors)
        print(f'{authors}<br />')

        abstract = note.content['abstract']

        print(f'<abstract>{abstract}</abstract>\n')

        print(f'[PDF]({pdf_url}) &bull;')

        if poster_url:
            print(f'[Poster]({poster_url}) &bull;')

        print(f'[Forum]({forum_url})')
        print('')

        print('<div style="text-align:center">\n&#10086;\n</div>')
        print('')



    raise 'heck'

    #for key in blind_notes:
    #    print(blind_notes[key])



    #print(len(all_decision_notes))

    accepted_submissions = [
        all_decision_notes[note.forum].details['original']
        for note in all_decision_notes if 'Spotlight' in note.content['decision']
    ]

    print(accepted_submissions)

    #author_emails = []
    #author_names = []
    #
    #print('')
    #
    #for submission in accepted_submissions:
    #    print(submission['content']['title'])
    #    print(submission['content']['authorids'])
    #    print(submission['content']['authors'])

    #print(openreview.tools.get_profile_info(
    #    client.get_profile('~Bastian_Rieck1'))
    #)

    #all_decision_notes = openreview.tools.iterget_notes(client, invitation = ‘auai.org/UAI/2019/Conference/-/Paper.*/Decision’)
    #
    #for review in tqdm(review_iterator, desc='Review'):
    #
    #    note_id = review.id
    #    paper_id = review.forum
    #
    #    os.makedirs(f'Data/2020/{paper_id}', exist_ok=True)
    #
    #    with open(f'Data/2020/{paper_id}/{note_id}.json', 'w') as f:
    #        json.dump(review.content, f)
