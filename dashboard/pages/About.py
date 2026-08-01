import streamlit as st

from utils import load_dataset

st.set_page_config(
    page_title="About AstraPredict",
    page_icon="🚀",
    layout="wide",
)

# ==================================================
# Load Dataset
# ==================================================

df = load_dataset()

# ==================================================
# Header
# ==================================================

st.title("🚀 About AstraPredict")

st.markdown(
    """
AstraPredict is an end-to-end machine learning application for exploring
historical space launches and predicting launch success using historical data.

The project combines **data engineering**, **machine learning**, **FastAPI**, and
**Streamlit** into a single interactive platform.
"""
)

st.divider()

# ==================================================
# Project Overview
# ==================================================

st.header("🌌 Project Overview")

left, right = st.columns([2, 1])

with left:

    st.markdown(
        """
### What AstraPredict Can Do

- 🚀 Explore over **4,000 historical launches**
- 🤖 Predict launch success using Machine Learning
- 📊 Interactive analytics dashboard
- 🌍 Explore launch providers and rockets
- 📈 Compare providers using historical data
- ⚙️ REST API powered by FastAPI
- 🧪 Inspect the ML model in Model Lab
"""
    )

with right:

    st.metric(
        "Historical Launches",
        f"{len(df):,}",
    )

    st.metric(
        "Providers",
        df["provider"].nunique(),
    )

    st.metric(
        "Rocket Variants",
        df["rocket"].nunique(),
    )

    st.metric(
        "Mission Types",
        df["mission_type"].nunique(),
    )

st.divider()

# ==================================================
# Technology Stack
# ==================================================

st.header("🛠 Technology Stack")

col1, col2 = st.columns(2)

with col1:

    st.markdown(
        """
### Backend

- Python
- FastAPI
- Scikit-learn
- Pandas
"""
    )

with col2:

    st.markdown(
        """
### Frontend

- Streamlit
- Plotly
- Joblib
"""
    )

st.divider()

# ==================================================
# Machine Learning
# ==================================================

st.header("🤖 Machine Learning Pipeline")

st.code(
"""
Historical Launch Dataset
          │
          ▼
Data Cleaning
          │
          ▼
Feature Engineering
          │
          ▼
Categorical Encoding
          │
          ▼
Logistic Regression
          │
          ▼
Launch Success Prediction
"""
)

st.divider()

# ==================================================
# Dataset
# ==================================================

st.header("📂 Dataset")

st.markdown(
    f"""
The application is currently powered by a cleaned historical dataset containing:

- **{len(df):,} launches**
- **{df['provider'].nunique()} launch providers**
- **{df['rocket'].nunique()} rocket variants**
- **{df['mission_type'].nunique()} mission categories**

This dataset spans several decades of launch history and powers all analytics,
historical insights, and machine learning predictions.
"""
)

st.divider()

# ==================================================
# Features
# ==================================================

st.header("✨ Key Features")

st.markdown(
"""
- 📊 Interactive Analytics
- 🚀 Launch Explorer
- 🛰 Mission Control
- ⚔️ Provider Comparison
- 🤖 AI Copilot
- 🧪 Model Lab
- 📈 Historical Intelligence
- ⚡ FastAPI Prediction API
"""
)

st.divider()

# ==================================================
# Footer
# ==================================================

st.success(
    "AstraPredict v1.0 • Built with Python, Streamlit, FastAPI & Scikit-learn 🚀"
)