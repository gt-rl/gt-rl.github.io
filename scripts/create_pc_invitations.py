"""Create invitations to programme commmittee."""


import pandas as pd
import sys


if __name__ == '__main__':
    df = pd.read_csv(sys.argv[1], sep='\t')

    # Print out people based on reviewing experience, but without e-mail
    # address.
    for group, df_ in df.groupby(df.columns[4]):
        print(group)
        print(df_.iloc[:, [1, 6]])
        print('')

    # Same content as above, but use format that is ready for
    # copy-and-paste to OpenReview backend.
    for group, df_ in df.groupby(df.columns[4]):
        print(group)

        for _, series  in df_.iterrows():
            print(f'{series.values[2]},{series.values[1]}')

        print('')
