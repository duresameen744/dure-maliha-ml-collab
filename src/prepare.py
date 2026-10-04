"""Prepare stage: load, clean, split, then encode (fit on train only)."""

from pathlib import Path

import pandas as pd
import yaml
from sklearn.model_selection import train_test_split

from src.data_cleaning import clean_adult_data

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "adult.csv"
PROCESSED = ROOT / "data" / "processed"


def main():
    with open(ROOT / "params.yaml") as f:
        params = yaml.safe_load(f)
    seed = params["seed"]
    test_size = params["split"]["test_size"]

    df = clean_adult_data(pd.read_csv(RAW))

    y = (df["class"] == ">50K").astype(int)
    X = df.drop(columns="class")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=seed, stratify=y
    )

    # Encode AFTER splitting: categories are learned from the training split only.
    X_train = pd.get_dummies(X_train, dtype=int)
    X_test = pd.get_dummies(X_test, dtype=int).reindex(
        columns=X_train.columns, fill_value=0
    )

    PROCESSED.mkdir(parents=True, exist_ok=True)
    X_train.to_csv(PROCESSED / "X_train.csv", index=False)
    X_test.to_csv(PROCESSED / "X_test.csv", index=False)
    y_train.to_csv(PROCESSED / "y_train.csv", index=False)
    y_test.to_csv(PROCESSED / "y_test.csv", index=False)
    print(f"Prepared: {len(X_train)} train rows, {len(X_test)} test rows")


if __name__ == "__main__":
    main()
