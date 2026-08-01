import streamlit as st


def show_rocket_stats(df, rocket_name):

    rocket_df = df[
        df["rocket"]
        .fillna("")
        .str.strip()
        .str.lower()
        ==
        rocket_name.strip().lower()
    ]

    if rocket_df.empty:

        rocket_df = df[
            df["rocket"]
            .fillna("")
            .str.contains(
                rocket_name,
                case=False,
                na=False,
            )
        ]

    if rocket_df.empty:
        st.warning(
            f"No historical data found for '{rocket_name}'."
        )
        return

    total_launches = len(
        rocket_df
    )

    providers = (
        rocket_df["provider"].nunique()
    )

    mission_types = (
        rocket_df["mission_type"].nunique()
    )

    first_year = int(
        rocket_df["year"].min()
    )

    latest_year = int(
        rocket_df["year"].max()
    )

    st.subheader("🚀 Rocket Intelligence")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "🚀 Total Launches",
            total_launches,
        )

        st.metric(
            "🏢 Providers",
            providers,
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
        f"Historical rocket: **{rocket_name}**"
    )