import streamlit as st


def show_kpi_cards(df):
    """Display high-level dataset metrics."""

    total_launches = len(df)
    total_providers = df["provider"].nunique()
    total_rockets = df["rocket"].nunique()
    total_missions = df["mission_type"].nunique()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "🚀 Total Launches",
        f"{total_launches:,}"
    )

    col2.metric(
        "🛰 Providers",
        total_providers
    )

    col3.metric(
        "🚀 Rocket Types",
        total_rockets
    )

    col4.metric(
        "🎯 Mission Types",
        total_missions
    )