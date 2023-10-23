import pandas as pd
import tracemalloc
import pickle
from pathlib import Path


def main():
    tracemalloc.start()

    snap = []
    snap.append(tracemalloc.get_traced_memory())

    load_df(Path('df1.df'))
    snap.append(tracemalloc.get_traced_memory())

    load_df(Path('df2.df'))
    snap.append(tracemalloc.get_traced_memory())

    df1 = load_df(Path('df1.df'))
    df2 = load_df(Path('df2.df'))
    snap.append(tracemalloc.get_traced_memory())

    for current, peak in snap:
        print(f"Current {int(current / 10 ** 6)} MB Peak {int(peak / 10 ** 6)} MB")


def load_df(df_filepath):
    raw_filepath = Path('data.txt')
    if df_filepath.exists():
        with open(df_filepath, 'rb') as f:
            return pickle.load(f)
    df = pd.read_csv(raw_filepath, dtype=dict(x='int32'))
    with open(df_filepath, 'wb') as f:
        pickle.dump(df, f)
    return df


if __name__ == '__main__':
    main()
