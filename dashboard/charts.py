import plotly.express as px
import streamlit as st


# ==================================================
# Launches Per Year
# ==================================================

def launches_by_year(df):

    chart = (
        df.groupby("year")
        .size()
        .reset_index(name="Launches")
    )

    fig = px.line(
        chart,
        x="year",
        y="Launches",
        markers=True,
        title="🚀 Launches Per Year",
    )

    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Launches",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )


# ==================================================
# Mission Distribution
# ==================================================

def mission_type_chart(df):

    chart = (
        df["mission_type"]
        .value_counts()
        .reset_index()
    )

    chart.columns = [
        "Mission",
        "Count",
    ]

    fig = px.pie(
        chart,
        values="Count",
        names="Mission",
        hole=0.45,
        title="🎯 Mission Distribution",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )


# ==================================================
# Top Providers
# ==================================================

def top_providers(df):

    chart = (
        df["provider"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    chart.columns = [
        "Provider",
        "Launches",
    ]

    fig = px.bar(
        chart,
        x="Launches",
        y="Provider",
        orientation="h",
        title="🛰 Top Launch Providers",
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


# ==================================================
# Top Rockets
# ==================================================

def top_rockets(df):

    chart = (
        df["rocket"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    chart.columns = [
        "Rocket",
        "Launches",
    ]

    fig = px.bar(
        chart,
        x="Launches",
        y="Rocket",
        orientation="h",
        title="🚀 Top Rockets",
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


# ==================================================
# Top Launch Pads
# ==================================================

def top_launch_pads(df):

    chart = (
        df["pad"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    chart.columns = [
        "Launch Pad",
        "Launches",
    ]

    fig = px.bar(
        chart,
        x="Launches",
        y="Launch Pad",
        orientation="h",
        title="📍 Top Launch Pads",
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