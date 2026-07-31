"""
Reusable provider leaderboard component.
"""

import pandas as pd
import streamlit as st


def show_provider_leaderboard(df: pd.DataFrame) -> None:
    """
    Display the top launch providers based on the
    number of launches in the dataset.
    """

    st.subheader("🏆 Top Launch Providers")

    provider_counts = (
        df["provider"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    provider_counts.columns = [
        "Provider",
        "Launches",
    ]

    st.dataframe(
        provider_counts,
        use_container_width=True,
        hide_index=True,
    )