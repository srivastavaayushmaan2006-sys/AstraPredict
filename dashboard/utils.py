from pathlib import Path

import pandas as pd
import requests

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "launches_features.csv"
)

API_URL = "http://127.0.0.1:8000/predict"


def load_dataset():
    """Load processed launch dataset."""

    return pd.read_csv(DATA_PATH)


def get_dataset_stats(df):
    """Return dashboard statistics."""

    return {
        "launches": len(df),
        "providers": df["provider"].nunique(),
        "rockets": df["rocket"].nunique(),
        "missions": df["mission_type"].nunique(),
    }


def predict(payload):
    """Call FastAPI prediction endpoint."""

    response = requests.post(
        API_URL,
        json=payload,
        timeout=10,
    )

    response.raise_for_status()

    return response.json()