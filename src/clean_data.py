"""Standalone script: clean the raw Adult Income dataset in place.

Removes exact duplicate rows and rows with missing values in
workclass, occupation, or native-country. Run once; the cleaned
file replaces data/raw/adult.csv and gets re-tracked with DVC.
"""

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "adult.csv"


def main():
    df = pd.read_csv(RAW)
    before = len(df)
    before_dupes = df.duplicated().sum()
    before_missing = df.isnull().sum().sum()

    df = df.drop_duplicates()
    df = df.dropna()

    after = len(df)

    print(f"Rows before: {before}")
    print(f"Duplicates removed: {before_dupes}")
    print(f"Missing-value rows removed: {before - before_dupes - after}")
    print(f"Total missing values before: {before_missing}")
    print(f"Rows after: {after}")

    df.to_csv(RAW, index=False)
    print(f"Saved cleaned data to {RAW}")


if __name__ == "__main__":
    main()
