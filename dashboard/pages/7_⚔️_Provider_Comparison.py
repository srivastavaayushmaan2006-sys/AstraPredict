import streamlit as st
import plotly.express as px

from utils import load_dataset

st.set_page_config(
    page_title="Provider Comparison",
    page_icon="⚔️",
    layout="wide",
)

df = load_dataset()

st.title("⚔️ Provider Comparison")

st.markdown(
    "Compare launch providers side-by-side."
)

providers = sorted(
    df["provider"].dropna().unique()
)

left, right = st.columns(2)

with left:

    provider1 = st.selectbox(
        "Provider A",
        providers,
        index=0,
    )

with right:

    default_index = 1 if len(providers) > 1 else 0

    provider2 = st.selectbox(
        "Provider B",
        providers,
        index=default_index,
    )

df1 = df[
    df["provider"] == provider1
]

df2 = df[
    df["provider"] == provider2
]

st.divider()
left, right = st.columns(2)

with left:

    st.subheader(provider1)

    st.metric(
        "🚀 Launches",
        len(df1),
    )

    st.metric(
        "🛰 Rockets",
        df1["rocket"].nunique(),
    )

    st.metric(
        "🎯 Mission Types",
        df1["mission_type"].nunique(),
    )

    st.metric(
        "📅 Years Active",
        f"{df1['year'].min()}–{df1['year'].max()}",
    )

with right:

    st.subheader(provider2)

    st.metric(
        "🚀 Launches",
        len(df2),
    )

    st.metric(
        "🛰 Rockets",
        df2["rocket"].nunique(),
    )

    st.metric(
        "🎯 Mission Types",
        df2["mission_type"].nunique(),
    )

    st.metric(
        "📅 Years Active",
        f"{df2['year'].min()}–{df2['year'].max()}",
    )
    st.divider()

trend = (
    df[
        df["provider"].isin(
            [provider1, provider2]
        )
    ]
    .groupby(
        ["year", "provider"]
    )
    .size()
    .reset_index(name="Launches")
)

fig = px.line(
    trend,
    x="year",
    y="Launches",
    color="provider",
    markers=True,
    title="Launches Over Time",
)

st.plotly_chart(
    fig,
    use_container_width=True,
)
st.divider()

missions = (
    df[
        df["provider"].isin(
            [provider1, provider2]
        )
    ]
    .groupby(
        [
            "provider",
            "mission_type",
        ]
    )
    .size()
    .reset_index(name="Launches")
)

fig = px.bar(
    missions,
    x="mission_type",
    y="Launches",
    color="provider",
    barmode="group",
    title="Mission Types",
)

st.plotly_chart(
    fig,
    use_container_width=True,
)