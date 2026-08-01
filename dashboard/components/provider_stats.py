import streamlit as st


def show_provider_stats(df, provider_name):

    provider_df = df[
        df["provider"]
        .fillna("")
        .str.strip()
        .str.lower()
        ==
        provider_name.strip().lower()
    ]

    if provider_df.empty:

        provider_df = df[
            df["provider"]
            .fillna("")
            .str.contains(
                provider_name,
                case=False,
                na=False,
            )
        ]

    if provider_df.empty:
        st.warning(
            f"No historical data found for '{provider_name}'."
        )
        return

    total_launches = len(provider_df)

    unique_rockets = (
        provider_df["rocket"].nunique()
    )

    mission_types = (
        provider_df["mission_type"].nunique()
    )

    first_year = int(
        provider_df["year"].min()
    )

    latest_year = int(
        provider_df["year"].max()
    )

    st.subheader("📈 Provider Intelligence")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "🚀 Total Launches",
            total_launches,
        )

        st.metric(
            "🛰 Rocket Types",
            unique_rockets,
        )

        st.metric(
            "🎯 Mission Types",
            mission_types,
        )

    with col2:

        st.metric(
            "📅 First Launch",
            first_year,
        )

        st.metric(
            "📆 Latest Launch",
            latest_year,
        )

        st.metric(
            "📈 Avg Launches / Year",
            round(
                total_launches
                / max(1, latest_year - first_year + 1),
                1,
            ),
        )

    st.caption(
        f"Historical provider: **{provider_name}**"
    )