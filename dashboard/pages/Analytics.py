import streamlit as st

from utils import load_dataset

from components.kpi_cards import show_kpi_cards

from charts import (
    launches_by_year,
    mission_type_chart,
    top_providers,
    top_rockets,
    top_launch_pads,
)

st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide",
)

# ==================================================
# Load Dataset
# ==================================================

df = load_dataset()

# ==================================================
# Header
# ==================================================

st.title("📊 AstraPredict Analytics")

st.markdown(
    "Explore historical launch trends using interactive analytics."
)

st.divider()

# ==================================================
# Sidebar Filters
# ==================================================

st.sidebar.header("🔎 Filters")

years = ["All"] + sorted(df["year"].unique().tolist())

selected_year = st.sidebar.selectbox(
    "Year",
    years,
)

if selected_year != "All":
    df = df[df["year"] == selected_year]

providers = ["All"] + sorted(
    df["provider"].dropna().unique().tolist()
)

selected_provider = st.sidebar.selectbox(
    "Provider",
    providers,
)

if selected_provider != "All":
    df = df[df["provider"] == selected_provider]

# ==================================================
# KPI Cards
# ==================================================

show_kpi_cards(df)

st.divider()

# ==================================================
# Charts
# ==================================================

left, right = st.columns(2)

with left:
    launches_by_year(df)
    top_providers(df)

with right:
    mission_type_chart(df)
    top_rockets(df)

st.divider()

top_launch_pads(df)

st.divider()

# ==================================================
# Search
# ==================================================

st.subheader("🔍 Search Historical Launches")

search = st.text_input(
    "Search by Mission Name",
)

if search:

    filtered = df[
        df["name"].str.contains(
            search,
            case=False,
            na=False,
        )
    ]

else:

    filtered = df

# ==================================================
# Data Table
# ==================================================

st.dataframe(
    filtered,
    use_container_width=True,
    hide_index=True,
)

st.caption(
    f"Showing {len(filtered):,} launches."
)

# ==================================================
# Download
# ==================================================

csv = filtered.to_csv(
    index=False,
).encode("utf-8")

st.download_button(
    "📥 Download Filtered Dataset",
    csv,
    file_name="filtered_launches.csv",
    mime="text/csv",
    use_container_width=True,
)