import streamlit as st

from utils import load_dataset
from charts import (
    launches_per_year,
    top_providers,
    top_rockets,
    mission_distribution,
)
from components.kpi_cards import show_kpi_cards
st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide",
)

st.title("📊 AstraPredict Analytics")

st.markdown(
    "Explore historical launch data with interactive charts."
)

st.divider()

df = load_dataset()

# --------------------------
# Sidebar Filters
# --------------------------

st.sidebar.header("Filters")

years = sorted(df["year"].unique())

selected_year = st.sidebar.selectbox(
    "Year",
    ["All"] + list(years)
)

if selected_year != "All":
    df = df[df["year"] == selected_year]

providers = sorted(df["provider"].unique())

selected_provider = st.sidebar.selectbox(
    "Provider",
    ["All"] + list(providers)
)

if selected_provider != "All":
    df = df[df["provider"] == selected_provider]

# --------------------------
# KPI Cards
# --------------------------

show_kpi_cards(df)

st.divider()

left, right = st.columns(2)

with left:
    launches_per_year(df)
    top_rockets(df)

with right:
    top_providers(df)
    mission_distribution(df)

st.divider()

st.subheader("🔍 Launch Explorer")

search = st.text_input(
    "Search by mission name"
)

if search:
    filtered = df[
        df["name"].str.contains(
            search,
            case=False,
            na=False
        )
    ]
else:
    filtered = df

st.dataframe(
    filtered,
    use_container_width=True,
    hide_index=True,
)

st.download_button(
    "📥 Download Filtered Dataset",
    filtered.to_csv(index=False),
    file_name="launches.csv",
)