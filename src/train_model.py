import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from src.config import MODEL_DIR, PROCESSED_DATA_DIR


def train_model():

    input_file = PROCESSED_DATA_DIR / "launches_features.csv"

    df = pd.read_csv(input_file)

    completed_status = [
        "Launch Successful",
        "Launch Failure",
        "Partial Failure",
    ]

    df = df[df["status"].isin(completed_status)]

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

    model = Pipeline(
        [
            ("preprocessor", preprocessor),
            ("classifier", LogisticRegression(max_iter=5000)),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    print("\nAccuracy")
    print("-" * 40)
    print(f"{accuracy_score(y_test, predictions):.3f}")

    print("\nConfusion Matrix")
    print("-" * 40)
    print(confusion_matrix(y_test, predictions))

    print("\nClassification Report")
    print("-" * 40)
    print(classification_report(y_test, predictions))

    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    model_path = MODEL_DIR / "launch_success_model.joblib"

    joblib.dump(model, model_path)

    print(f"\nModel saved to:\n{model_path}")


if __name__ == "__main__":
    train_model()