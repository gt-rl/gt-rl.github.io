import pandas as pd
import sys

if __name__ == "__main__":
    filename = sys.argv[1]

    top_k = 20

    df = pd.read_csv(filename)
    df.set_index("number", inplace=True)

    decision = "Accept (Paper)"
    df = df[df.decision == decision]
    df = df.sort_values(by="average rating", ascending=False)

    for index, row in df.head(n=top_k).iterrows():
        print(row["authorids"])
