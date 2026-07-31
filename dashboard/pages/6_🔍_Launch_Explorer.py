import streamlit as st

from utils import load_dataset
from components.kpi_cards import show_kpi_cards

st.set_page_config(
    page_title="Launch Explorer",
    page_icon="🔍",
    layout="wide",
)

df = load_dataset()

st.title("🔍 Launch Explorer")

st.markdown(
    "Explore every historical launch in the AstraPredict dataset."
)

show_kpi_cards(df)

st.divider()

# ============================================
# Sidebar Filters
# ============================================

st.sidebar.header("Filters")

providers = ["All"] + sorted(
    df["provider"].dropna().unique().tolist()
)

provider = st.sidebar.selectbox(
    "Provider",
    providers,
)

filtered = df.copy()

if provider != "All":

    filtered = filtered[
        filtered["provider"] == provider
    ]

rockets = ["All"] + sorted(
    filtered["rocket"].dropna().unique().tolist()
)

rocket = st.sidebar.selectbox(
    "Rocket",
    rockets,
)

if rocket != "All":

    filtered = filtered[
        filtered["rocket"] == rocket
    ]

missions = ["All"] + sorted(
    filtered["mission_type"].dropna().unique().tolist()
)

mission = st.sidebar.selectbox(
    "Mission Type",
    missions,
)

if mission != "All":

    filtered = filtered[
        filtered["mission_type"] == mission
    ]

years = ["All"] + sorted(
    filtered["year"].unique().tolist()
)

year = st.sidebar.selectbox(
    "Year",
    years,
)

if year != "All":

    filtered = filtered[
        filtered["year"] == year
    ]

# ============================================
# Results
# ============================================

st.subheader("Matching Launches")

st.metric(
    "Results",
    len(filtered),
)

st.dataframe(
    filtered[
        [
            "name",
            "provider",
            "rocket",
            "mission_type",
            "pad",
            "year",
            "status",
        ]
    ],
    use_container_width=True,
    hide_index=True,
)