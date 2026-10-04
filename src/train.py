"""Train stage: fit a Random Forest on the prepared training split."""

import pickle
from pathlib import Path

import pandas as pd
import yaml
from sklearn.ensemble import RandomForestClassifier

ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
MODELS = ROOT / "models"


def main():
    with open(ROOT / "params.yaml") as f:
        params = yaml.safe_load(f)
    seed = params["seed"]
    n_estimators = params["train"]["n_estimators"]
    max_depth = params["train"]["max_depth"]

    X_train = pd.read_csv(PROCESSED / "X_train.csv")
    y_train = pd.read_csv(PROCESSED / "y_train.csv").squeeze("columns")

    model = RandomForestClassifier(
        n_estimators=n_estimators, max_depth=max_depth, random_state=seed
    )
    model.fit(X_train, y_train)

    MODELS.mkdir(parents=True, exist_ok=True)
    with open(MODELS / "model.pkl", "wb") as f:
        pickle.dump(model, f)
    print(f"Trained model saved to {MODELS / 'model.pkl'}")


if __name__ == "__main__":
    main()
