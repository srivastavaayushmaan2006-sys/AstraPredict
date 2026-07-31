import streamlit as st
import plotly.express as px

from model_metrics import (
    load_metrics,
    load_confusion_matrix,
    load_classification_report,
)
st.set_page_config(
    page_title="Model Insights",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 Model Insights")

st.markdown(
    """
Understand how the machine learning model performs using
evaluation metrics and detailed reports.
"""
)

st.divider()

# --------------------------------------------------
# Load Data
# --------------------------------------------------

metrics = load_metrics()
cm = load_confusion_matrix()
report = load_classification_report()

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Accuracy",
    f"{metrics['accuracy']:.2%}",
)

col2.metric(
    "Precision",
    f"{metrics['precision']:.2%}",
)

col3.metric(
    "Recall",
    f"{metrics['recall']:.2%}",
)

col4.metric(
    "F1 Score",
    f"{metrics['f1_score']:.2%}",
)

st.divider()

# --------------------------------------------------
# Charts
# --------------------------------------------------

left, right = st.columns(2)

with left:

    st.subheader("📊 Confusion Matrix")

    fig = px.imshow(
        cm,
        text_auto=True,
        aspect="auto",
        labels=dict(
            x="Predicted",
            y="Actual",
            color="Count",
        ),
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

with right:

    st.subheader("📄 Classification Report")

    st.dataframe(
        report,
        use_container_width=True,
    )

st.divider()

# --------------------------------------------------
# Metric Explanation
# --------------------------------------------------

st.subheader("📚 Metric Guide")

with st.expander("Accuracy"):
    st.write(
        """
Accuracy measures the percentage of total predictions
that were correct.
"""
    )

with st.expander("Precision"):
    st.write(
        """
Precision answers:

Out of all launches predicted as successful,
how many were actually successful?
"""
    )

with st.expander("Recall"):
    st.write(
        """
Recall answers:

Out of all successful launches,
how many did the model correctly identify?
"""
    )

with st.expander("F1 Score"):
    st.write(
        """
The F1 Score balances Precision and Recall
into a single metric.
"""
    )

st.divider()

st.caption(
    "🚀 AstraPredict • Machine Learning Evaluation Dashboard"
)