import json
import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score,
    roc_curve,
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
            (
                "classifier",
                LogisticRegression(
                    max_iter=5000,
                    random_state=42,
                ),
            ),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    print("Training model...")

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]

    accuracy = accuracy_score(
        y_test,
        predictions,
    )

    roc_auc = roc_auc_score(
        y_test,
        probabilities,
    )

    report = classification_report(
        y_test,
        predictions,
        output_dict=True,
    )

    cm = confusion_matrix(
        y_test,
        predictions,
    )

    print("\nAccuracy")
    print("-" * 40)
    print(f"{accuracy:.3f}")

    print("\nROC AUC")
    print("-" * 40)
    print(f"{roc_auc:.3f}")

    print("\nConfusion Matrix")
    print("-" * 40)
    print(cm)

    print("\nClassification Report")
    print("-" * 40)
    print(
        classification_report(
            y_test,
            predictions,
        )
    )

    MODEL_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    # -------------------------------------------------
    # Save trained model
    # -------------------------------------------------

    model_path = (
        MODEL_DIR
        / "launch_success_model.joblib"
    )

    joblib.dump(
        model,
        model_path,
    )

    # -------------------------------------------------
    # Save metrics
    # -------------------------------------------------

    metrics = {
        "model": "Logistic Regression",
        "accuracy": float(accuracy),
        "precision": float(
            report["1"]["precision"]
        ),
        "recall": float(
            report["1"]["recall"]
        ),
        "f1_score": float(
            report["1"]["f1-score"]
        ),
        "roc_auc": float(
            roc_auc
        ),
        "training_samples": len(
            X_train
        ),
        "testing_samples": len(
            X_test
        ),
        "dataset_size": len(
            df
        ),
        "features": len(
            feature_columns
        ),
    }

    with open(
        MODEL_DIR / "metrics.json",
        "w",
    ) as f:

        json.dump(
            metrics,
            f,
            indent=4,
        )

    # -------------------------------------------------
    # Save confusion matrix
    # -------------------------------------------------

    cm_df = pd.DataFrame(
        cm,
        index=[
            "Actual Failure",
            "Actual Success",
        ],
        columns=[
            "Predicted Failure",
            "Predicted Success",
        ],
    )

    cm_df.to_csv(
        MODEL_DIR
        / "confusion_matrix.csv"
    )

    # -------------------------------------------------
    # Save classification report
    # -------------------------------------------------

    report_df = (
        pd.DataFrame(report)
        .transpose()
    )

    report_df.to_csv(
        MODEL_DIR
        / "classification_report.csv"
    )

    # -------------------------------------------------
    # Save test predictions
    # -------------------------------------------------

    results = X_test.copy()

    results["Actual"] = y_test.values
    results["Predicted"] = predictions
    results["Probability"] = probabilities

    results.to_csv(
        MODEL_DIR
        / "test_predictions.csv",
        index=False,
    )

    # -------------------------------------------------
    # Save ROC Curve
    # -------------------------------------------------

    fpr, tpr, thresholds = roc_curve(
        y_test,
        probabilities,
    )

    roc_df = pd.DataFrame(
        {
            "False Positive Rate": fpr,
            "True Positive Rate": tpr,
            "Threshold": thresholds,
        }
    )

    roc_df.to_csv(
        MODEL_DIR
        / "roc_curve.csv",
        index=False,
    )

    # -------------------------------------------------
    # Save Training Information
    # -------------------------------------------------

    training_info = {
        "algorithm": "Logistic Regression",
        "categorical_features": categorical,
        "numeric_features": numeric,
        "training_rows": len(
            X_train
        ),
        "testing_rows": len(
            X_test
        ),
        "dataset_rows": len(
            df
        ),
    }

    with open(
        MODEL_DIR
        / "training_info.json",
        "w",
    ) as f:

        json.dump(
            training_info,
            f,
            indent=4,
        )

    print("\nModel saved to:")
    print(model_path)

    print("\nGenerated files:")
    print("✓ metrics.json")
    print("✓ confusion_matrix.csv")
    print("✓ classification_report.csv")
    print("✓ test_predictions.csv")
    print("✓ roc_curve.csv")
    print("✓ training_info.json")

    print("\nTraining complete!")


if __name__ == "__main__":
    train_model()