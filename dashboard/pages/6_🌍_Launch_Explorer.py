import streamlit as st

from utils import load_dataset

from components.kpi_cards import show_kpi_cards
from components.charts import (
    launches_by_year,
    mission_type_chart,
    top_providers,
    top_rockets,
    top_launch_pads,
)

st.set_page_config(
    page_title="Launch Explorer",
    page_icon="🔍",
    layout="wide",
)

# ==================================================
# Load Dataset
# ==================================================

df = load_dataset()

# ==================================================
# Header
# ==================================================

st.title("🔍 Launch Explorer")

st.markdown(
    "Explore every historical launch in the AstraPredict dataset."
)

show_kpi_cards(df)

st.divider()

# ==================================================
# Sidebar Filters
# ==================================================

st.sidebar.header("🔎 Filters")

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

# ==================================================
# Empty Results
# ==================================================

if filtered.empty:

    st.warning(
        "No launches match the selected filters."
    )

    st.stop()

# ==================================================
# Results Summary
# ==================================================

st.subheader("📊 Filter Results")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🚀 Launches",
        len(filtered),
    )

with col2:
    st.metric(
        "🛰 Providers",
        filtered["provider"].nunique(),
    )

with col3:
    st.metric(
        "🚀 Rockets",
        filtered["rocket"].nunique(),
    )

with col4:
    st.metric(
        "🎯 Mission Types",
        filtered["mission_type"].nunique(),
    )

st.divider()

# ==================================================
# Charts
# ==================================================

chart1, chart2 = st.columns(2)

with chart1:
    launches_by_year(filtered)

with chart2:
    mission_type_chart(filtered)

st.divider()

chart3, chart4 = st.columns(2)

with chart3:
    top_providers(filtered)

with chart4:
    top_rockets(filtered)

st.divider()

top_launch_pads(filtered)

st.divider()

# ==================================================
# Mission Explorer
# ==================================================

st.subheader("🚀 Mission Explorer")

mission_names = filtered["name"].tolist()

selected_mission = st.selectbox(
    "Select a Historical Launch",
    mission_names,
)

mission = filtered[
    filtered["name"] == selected_mission
].iloc[0]

left, right = st.columns([2, 1])

with left:

    st.markdown("### 📖 Mission Details")

    st.write(
        f"**Mission:** {mission['name']}"
    )

    st.write(
        f"**Provider:** {mission['provider']}"
    )

    st.write(
        f"**Rocket:** {mission['rocket']}"
    )

    st.write(
        f"**Mission Type:** {mission['mission_type']}"
    )

    st.write(
        f"**Launch Pad:** {mission['pad']}"
    )

    st.write(
        f"**Launch Year:** {mission['year']}"
    )

    st.write(
        f"**Status:** {mission['status']}"
    )

with right:

    st.metric(
        "📅 Year",
        mission["year"],
    )

    st.metric(
        "🚀 Provider",
        mission["provider"],
    )

    st.metric(
        "🛰 Rocket",
        mission["rocket"],
    )

    st.metric(
        "📍 Launch Pad",
        mission["pad"],
    )

st.divider()

# ==================================================
# Download
# ==================================================

csv = filtered.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Results",
    data=csv,
    file_name="filtered_launches.csv",
    mime="text/csv",
    use_container_width=True,
)

st.divider()

# ==================================================
# Historical Launch Table
# ==================================================

st.subheader("📋 Historical Launches")

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

st.caption(
    f"Showing {len(filtered):,} historical launches."
)