"""
AstraPredict Dashboard
Landing page for the AstraPredict platform.
"""

import streamlit as st

from components.feature_card import show_feature_card
from components.footer import show_footer
from components.hero import show_hero
from components.metrics import show_metrics
from components.provider_card import show_provider_leaderboard
from utils import (
    get_dataset_stats,
    load_dataset,
)

# ---------------------------------------
# Page Config
# ---------------------------------------

st.set_page_config(
    page_title="AstraPredict",
    page_icon="🚀",
    layout="wide",
)

# ---------------------------------------
# Load CSS
# ---------------------------------------

with open("dashboard/assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True,
    )

# ---------------------------------------
# Load Dataset
# ---------------------------------------

df = load_dataset()
stats = get_dataset_stats(df)

# ---------------------------------------
# Hero Section
# ---------------------------------------

show_hero()

st.divider()

# ---------------------------------------
# Dashboard Metrics
# ---------------------------------------

show_metrics(stats)

st.divider()

# ---------------------------------------
# Feature Overview
# ---------------------------------------

left, right = st.columns(2)

with left:
    show_feature_card(
        title="Prediction",
        icon="🔮",
        description="Predict the probability of a successful launch using our trained machine learning model.",
        features=[
            "Success probability",
            "Confidence score",
            "FastAPI backend",
            "Historical launch data",
        ],
    )

with right:
    show_feature_card(
        title="Analytics",
        icon="📊",
        description="Explore historical launch data with interactive visualizations.",
        features=[
            "Provider statistics",
            "Rocket trends",
            "Mission types",
            "Historical launches",
        ],
    )

st.divider()

# ---------------------------------------
# Top Launch Providers
# ---------------------------------------

show_provider_leaderboard(df)

st.divider()

# ---------------------------------------
# Technology Stack
# ---------------------------------------

st.subheader("⚙️ Technology Stack")

tech1, tech2, tech3, tech4 = st.columns(4)

tech1.info("🐍 Python")
tech2.info("⚡ FastAPI")
tech3.info("🎈 Streamlit")
tech4.info("🤖 Scikit-Learn")

st.divider()

# ---------------------------------------
# Getting Started
# ---------------------------------------

st.success(
    """
👈 Use the sidebar to navigate through the application.

Start with **Predict** to estimate launch success or explore the
**Analytics** page to discover trends in historical launch data.
"""
)

st.divider()

# ---------------------------------------
# Footer
# ---------------------------------------

show_footer()