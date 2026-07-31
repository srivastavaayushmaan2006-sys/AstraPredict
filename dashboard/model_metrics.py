import json
from pathlib import Path

import pandas as pd

MODEL_DIR = Path("models")


def load_metrics():
    with open(MODEL_DIR / "metrics.json", "r") as f:
        return json.load(f)


def load_confusion_matrix():
    return pd.read_csv(
        MODEL_DIR / "confusion_matrix.csv",
        index_col=0,
    )


def load_classification_report():
    return pd.read_csv(
        MODEL_DIR / "classification_report.csv",
        index_col=0,
    )


def load_predictions():
    return pd.read_csv(
        MODEL_DIR / "test_predictions.csv"
    )