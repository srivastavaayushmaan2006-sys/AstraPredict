import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

from src.config import PROCESSED_DATA_DIR


COMPLETED_STATUS = [
    "Launch Successful",
    "Launch Failure",
    "Partial Failure",
]


FEATURE_COLUMNS = [
    "provider",
    "rocket",
    "mission_type",
    "pad",
    "year",
    "month",
    "day",
    "hour",
]


def load_training_data():

    df = pd.read_csv(
        PROCESSED_DATA_DIR / "launches_features.csv"
    )

    df = df[df["status"].isin(COMPLETED_STATUS)]

    df["success"] = (
        df["status"] == "Launch Successful"
    ).astype(int)

    X = df[FEATURE_COLUMNS]
    y = df["success"]

    categorical = [
        "provider",
        "rocket",
        "mission_type",
        "pad",
    ]

    numeric = [
        "year",
        "month",
        "day",
        "hour",
    ]

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "cat",
                OneHotEncoder(handle_unknown="ignore"),
                categorical,
            ),
            (
                "num",
                "passthrough",
                numeric,
            ),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    return (
        X_train,
        X_test,
        y_train,
        y_test,
        preprocessor,
    )