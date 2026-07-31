from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier

from src.ml_utils import load_training_data


def evaluate(name, classifier):

    (
        X_train,
        X_test,
        y_train,
        y_test,
        preprocessor,
    ) = load_training_data()

    model = Pipeline(
        [
            ("preprocessor", preprocessor),
            ("classifier", classifier),
        ]
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    score = accuracy_score(
        y_test,
        predictions,
    )

    return score


def main():

    models = {
        "Logistic Regression": LogisticRegression(max_iter=5000),
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "Random Forest": RandomForestClassifier(
            random_state=42,
            n_estimators=200,
        ),
    }

    print("\nModel Comparison")
    print("=" * 40)

    for name, model in models.items():

        score = evaluate(name, model)

        print(f"{name:<25} {score:.3f}")


if __name__ == "__main__":
    main()