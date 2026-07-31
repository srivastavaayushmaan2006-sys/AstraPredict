import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from src.config import PROCESSED_DATA_DIR


def prepare_dataset():

    input_file = PROCESSED_DATA_DIR / "launches_features.csv"

    df = pd.read_csv(input_file)

    print(f"Loaded {len(df)} rows")

    # ---------------------------------
    # Keep only completed launches
    # ---------------------------------

    completed_status = [
        "Launch Successful",
        "Launch Failure",
        "Partial Failure"
    ]

    df = df[df["status"].isin(completed_status)]

    print(f"Completed launches: {len(df)}")

    # Binary target

    df["success"] = (
        df["status"] == "Launch Successful"
    ).astype(int)

    feature_columns = [
        "provider",
        "rocket",
        "mission_type",
        "pad",
        "year",
        "month",
        "day",
        "hour",
    ]

    X = df[feature_columns]
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

    pipeline = Pipeline(
        [
            ("preprocessor", preprocessor),
        ]
    )

    pipeline.fit(X_train)

    X_train = pipeline.transform(X_train)
    X_test = pipeline.transform(X_test)

    joblib.dump(
        pipeline,
        PROCESSED_DATA_DIR / "preprocessing_pipeline.joblib",
    )

    print("\nTraining samples:", X_train.shape)
    print("Testing samples:", X_test.shape)

    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    prepare_dataset()