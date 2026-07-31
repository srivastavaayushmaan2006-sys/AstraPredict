from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

DATA_PATH = Path("data/processed/launches.csv")


@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)


def launches_by_year():

    df = load_data()

    yearly = (
        df.groupby("year")
        .size()
        .reset_index(name="Launches")
    )

    fig = px.line(
        yearly,
        x="year",
        y="Launches",
        markers=True,
        title="Launches Per Year",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )


def mission_type_chart():

    df = load_data()

    mission_counts = (
        df["mission_type"]
        .value_counts()
        .reset_index()
    )

    mission_counts.columns = [
        "Mission",
        "Count",
    ]

    fig = px.pie(
        mission_counts,
        values="Count",
        names="Mission",
        hole=0.45,
        title="Mission Type Distribution",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )


def top_providers():

    df = load_data()

    providers = (
        df["provider"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    providers.columns = [
        "Provider",
        "Launches",
    ]

    fig = px.bar(
        providers,
        x="Launches",
        y="Provider",
        orientation="h",
        title="Top 10 Launch Providers",
    )

    fig.update_layout(
        yaxis=dict(
            categoryorder="total ascending"
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )