"""Evaluate stage: score the trained model on the test split."""

import json
import pickle
import subprocess
from pathlib import Path

import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
MODELS = ROOT / "models"


def get_git_sha():
    try:
        return (
            subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT)
            .decode()
            .strip()
        )
    except (subprocess.CalledProcessError, OSError):
        return "unknown"


def main():
    X_test = pd.read_csv(PROCESSED / "X_test.csv")
    y_test = pd.read_csv(PROCESSED / "y_test.csv").squeeze("columns")

    with open(MODELS / "model.pkl", "rb") as f:
        model = pickle.load(f)

    y_pred = model.predict(X_test)

    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1": f1_score(y_test, y_pred),
        "commit_sha": get_git_sha(),
    }

    with open(ROOT / "metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
