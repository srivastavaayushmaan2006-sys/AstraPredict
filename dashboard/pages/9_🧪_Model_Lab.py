import json

import joblib
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from pathlib import Path
MODEL_DIR = Path("models")
from utils import load_dataset

st.set_page_config(
    page_title="Model Lab",
    page_icon="🧪",
    layout="wide",
)

# ==================================================
# Header
# ==================================================

st.title("🧪 AstraPredict Model Lab")

st.markdown(
    """
Explore the machine learning model powering AstraPredict.

This page displays the trained model,
evaluation metrics,
confusion matrix,
ROC curve,
and training metadata.
"""
)

# ==================================================
# Load Dataset
# ==================================================

df = load_dataset()

# ==================================================
# Load Model
# ==================================================

model = joblib.load(
    MODEL_DIR / "launch_success_model.joblib"
)

# ==================================================
# Load Saved Files
# ==================================================

metrics = None
cm = None
report = None
roc = None
training = None

try:

    with open(
        MODEL_DIR / "metrics.json",
        "r",
    ) as f:

        metrics = json.load(f)

except Exception:
    pass

try:

    cm = pd.read_csv(
        MODEL_DIR / "confusion_matrix.csv",
        index_col=0,
    )

except Exception:
    pass

try:

    report = pd.read_csv(
        MODEL_DIR / "classification_report.csv",
        index_col=0,
    )

except Exception:
    pass

try:

    roc = pd.read_csv(
        MODEL_DIR / "roc_curve.csv"
    )

except Exception:
    pass

try:

    with open(
        MODEL_DIR / "training_info.json",
        "r",
    ) as f:

        training = json.load(f)

except Exception:
    pass

# ==================================================
# Model Information
# ==================================================

st.header("🤖 Model Information")

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "Model",
        type(model).__name__,
    )

with c2:

    st.metric(
        "Dataset Rows",
        f"{len(df):,}",
    )

with c3:

    st.metric(
        "Features",
        len(df.columns),
    )

st.divider()

# ==================================================
# Metrics
# ==================================================

st.header("📊 Evaluation Metrics")

if metrics:

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Accuracy",
        f"{metrics['accuracy']:.2%}",
    )

    c2.metric(
        "Precision",
        f"{metrics['precision']:.2%}",
    )

    c3.metric(
        "Recall",
        f"{metrics['recall']:.2%}",
    )

    c4.metric(
        "ROC-AUC",
        f"{metrics['roc_auc']:.2%}",
    )

else:

    st.warning(
        "metrics.json not found."
    )

st.divider()

# ==================================================
# Confusion Matrix
# ==================================================

st.header("🔥 Confusion Matrix")

if cm is not None:

    fig = px.imshow(
        cm,
        text_auto=True,
        color_continuous_scale="Blues",
        aspect="auto",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

else:

    st.info(
        "confusion_matrix.csv not found."
    )

st.divider()

# ==================================================
# ROC Curve
# ==================================================

st.header("📈 ROC Curve")

if roc is not None:

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=roc["False Positive Rate"],
            y=roc["True Positive Rate"],
            mode="lines",
            name="ROC Curve",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[0, 1],
            y=[0, 1],
            mode="lines",
            name="Random",
            line=dict(
                dash="dash",
            ),
        )
    )

    fig.update_layout(
        xaxis_title="False Positive Rate",
        yaxis_title="True Positive Rate",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

else:

    st.info(
        "roc_curve.csv not found."
    )

st.divider()

# ==================================================
# Classification Report
# ==================================================

st.header("📋 Classification Report")

if report is not None:

    st.dataframe(
        report,
        use_container_width=True,
    )

else:

    st.info(
        "classification_report.csv not found."
    )

st.divider()

# ==================================================
# Training Information
# ==================================================

st.header("⚙️ Training Information")

if training:

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Algorithm",
        training["algorithm"],
    )

    c2.metric(
        "Training Rows",
        training["training_rows"],
    )

    c3.metric(
        "Testing Rows",
        training["testing_rows"],
    )

    st.write(
        "**Categorical Features**"
    )

    st.write(
        training["categorical_features"]
    )

    st.write(
        "**Numeric Features**"
    )

    st.write(
        training["numeric_features"]
    )

else:

    st.info(
        "training_info.json not found."
    )

st.divider()

# ==================================================
# Dataset Overview
# ==================================================

st.header("📁 Dataset Overview")

left, right = st.columns(2)

with left:

    st.metric(
        "Providers",
        df["provider"].nunique(),
    )

    st.metric(
        "Rocket Types",
        df["rocket"].nunique(),
    )

with right:

    st.metric(
        "Mission Types",
        df["mission_type"].nunique(),
    )

    st.metric(
        "Launches",
        len(df),
    )

st.divider()

# ==================================================
# ML Pipeline
# ==================================================

st.header("⚙️ Machine Learning Pipeline")

st.code(
"""
Historical Launch Dataset
        ↓
Feature Engineering
        ↓
One-Hot Encoding
        ↓
Train/Test Split
        ↓
Logistic Regression
        ↓
Model Evaluation
        ↓
FastAPI Prediction API
        ↓
Mission Control Dashboard
"""
)

st.divider()

# ==================================================
# Dataset Preview
# ==================================================

st.header("📝 Dataset Preview")

st.dataframe(
    df.head(10),
    use_container_width=True,
)

st.divider()

st.success(
    "🚀 Model Lab loaded successfully."
)