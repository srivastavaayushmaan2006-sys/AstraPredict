"""
Reusable hero section for AstraPredict.
"""

import streamlit as st


def show_hero() -> None:
    """
    Display the landing page hero section.
    """

    st.title("🚀 AstraPredict")

    st.markdown(
        """
# AI-Powered Space Mission Analytics Platform

AstraPredict combines **Machine Learning**, **Data Analytics**, and **Interactive Dashboards**
to explore historical launch data and predict mission outcomes.

### What you can do

-   Predict launch success
-   Explore launch analytics
-   Understand machine learning models
-   Discover trends in space missions
"""
    )