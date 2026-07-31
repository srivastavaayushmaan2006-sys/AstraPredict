import streamlit as st


def stars(value, thresholds):
    """
    Convert a numeric value into a 1-5 star rating.

    thresholds example:
    [10, 50, 100, 200]
    """

    if value >= thresholds[3]:
        return "★★★★★"

    elif value >= thresholds[2]:
        return "★★★★☆"

    elif value >= thresholds[1]:
        return "★★★☆☆"

    elif value >= thresholds[0]:
        return "★★☆☆☆"

    else:
        return "★☆☆☆☆"


def generate_summary(
    provider,
    rocket,
    probability,
    provider_launches,
    rocket_launches,
    mission_launches,
):
    """
    Generate a readable AI summary based on
    historical dataset statistics.
    """

    summary = []

    summary.append(
        f"**{provider}** has completed "
        f"**{provider_launches:,}** recorded launches."
    )

    summary.append(
        f"The **{rocket}** rocket appears in "
        f"**{rocket_launches:,}** historical missions."
    )

    summary.append(
        f"This mission profile has appeared "
        f"**{mission_launches:,}** times in the dataset."
    )

    if probability >= 0.90:

        summary.append(
            "The model predicts a **very high probability of success**. "
            "This launch shares characteristics with many historical missions."
        )

    elif probability >= 0.75:

        summary.append(
            "The model predicts a **high probability of success**, "
            "although some uncertainty remains."
        )

    elif probability >= 0.60:

        summary.append(
            "The prediction indicates **moderate confidence**. "
            "Historical patterns are somewhat mixed."
        )

    else:

        summary.append(
            "The prediction has **lower confidence**. "
            "Similar launches are less common or have more varied outcomes."
        )

    return "\n\n".join(summary)


def show_ai_insights(df, launch, prediction):

    probability = prediction["success_probability"]

    provider_launches = len(
        df[df["provider"] == launch["provider"]]
    )

    rocket_launches = len(
        df[df["rocket"] == launch["rocket"]]
    )

    mission_launches = len(
        df[df["mission_type"] == launch["mission"]]
    )

    st.subheader("🧠 AI Mission Intelligence")

    # ==================================================
    # Confidence
    # ==================================================

    if probability >= 0.90:

        confidence = "🟢 Very High"
        risk = "🟢 Low"

    elif probability >= 0.75:

        confidence = "🔵 High"
        risk = "🔵 Moderate"

    elif probability >= 0.60:

        confidence = "🟡 Moderate"
        risk = "🟡 Moderate"

    else:

        confidence = "🔴 Low"
        risk = "🔴 Elevated"

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Model Confidence",
            confidence,
        )

    with col2:

        st.metric(
            "Risk Level",
            risk,
        )

    st.divider()

    # ==================================================
    # Experience Ratings
    # ==================================================

    st.markdown("### ⭐ Historical Experience")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Provider Experience",
            stars(
                provider_launches,
                [10, 50, 100, 200],
            ),
        )

    with c2:

        st.metric(
            "Rocket Familiarity",
            stars(
                rocket_launches,
                [10, 30, 75, 150],
            ),
        )

    with c3:

        st.metric(
            "Mission Frequency",
            stars(
                mission_launches,
                [5, 20, 50, 100],
            ),
        )

    st.divider()

    # ==================================================
    # Historical Context
    # ==================================================

    st.markdown("### 📊 Historical Context")

    st.info(
        f"🚀 Provider launches: **{provider_launches:,}**"
    )

    st.info(
        f"🛰 Rocket launches: **{rocket_launches:,}**"
    )

    st.info(
        f"🎯 Similar mission types: **{mission_launches:,}**"
    )

    st.info(
        f"📅 Scheduled launch year: **{launch['year']}**"
    )

    st.divider()

    # ==================================================
    # AI Summary
    # ==================================================

    st.markdown("### 🤖 AI Summary")

    summary = generate_summary(
        provider=launch["provider"],
        rocket=launch["rocket"],
        probability=probability,
        provider_launches=provider_launches,
        rocket_launches=rocket_launches,
        mission_launches=mission_launches,
    )

    st.markdown(summary)

    st.caption(
        "These insights summarize historical patterns in the dataset and "
        "the model's predicted probability. They are not causal explanations "
        "of the machine learning model."
    )