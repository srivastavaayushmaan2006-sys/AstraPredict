import streamlit as st


def show_provider_stats(df, provider_name):

    provider_df = df[df["provider"] == provider_name]

    if provider_df.empty:
        st.warning("No historical data available.")
        return

    total_launches = len(provider_df)
    unique_rockets = provider_df["rocket"].nunique()
    mission_types = provider_df["mission_type"].nunique()
    first_year = int(provider_df["year"].min())
    latest_year = int(provider_df["year"].max())

    st.subheader("📈 Provider Intelligence")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("🚀 Total Launches", total_launches)
        st.metric("🛰 Unique Rockets", unique_rockets)
        st.metric("📡 Mission Types", mission_types)

    with col2:
        st.metric("📅 First Launch", first_year)
        st.metric("📆 Latest Launch", latest_year)