import streamlit as st

from utils import load_dataset

st.set_page_config(
    page_title="AstraPredict Copilot",
    page_icon="🤖",
    layout="wide",
)

df = load_dataset()

st.title("🤖 AstraPredict Copilot")

st.markdown(
    """
Ask questions about the historical launch dataset.

Examples:

• Which provider has the most launches?

• What is the most used rocket?

• Which mission type is most common?

• Which year had the most launches?

• Tell me about SpaceX

• Tell me about Falcon 9
"""
)

question = st.text_input(
    "Ask a question",
    placeholder="Which provider has the most launches?",
)

if st.button("Ask AI"):

    if not question.strip():

        st.warning("Please enter a question.")

        st.stop()

    q = question.lower()

    answer = None

    # ==================================================
    # Most Launches
    # ==================================================

    if "most launches" in q and "provider" in q:

        provider = df["provider"].value_counts().idxmax()

        launches = df["provider"].value_counts().max()

        answer = (
            f"🚀 **{provider}** has the most recorded launches "
            f"with **{launches:,}** missions."
        )

    # ==================================================
    # Most Used Rocket
    # ==================================================

    elif "rocket" in q and (
        "most" in q or "used" in q
    ):

        rocket = df["rocket"].value_counts().idxmax()

        launches = df["rocket"].value_counts().max()

        answer = (
            f"🛰 **{rocket}** is the most frequently used rocket "
            f"with **{launches:,}** launches."
        )

    # ==================================================
    # Most Common Mission
    # ==================================================

    elif "mission" in q:

        mission = df["mission_type"].value_counts().idxmax()

        launches = df["mission_type"].value_counts().max()

        answer = (
            f"🎯 **{mission}** is the most common mission type "
            f"with **{launches:,}** launches."
        )

    # ==================================================
    # Busiest Year
    # ==================================================

    elif "year" in q:

        year = df["year"].value_counts().idxmax()

        launches = df["year"].value_counts().max()

        answer = (
            f"📅 **{year}** recorded the most launches "
            f"with **{launches:,}** missions."
        )

    # ==================================================
    # Provider Search
    # ==================================================

    else:

        found = False

        for provider in df["provider"].dropna().unique():

            if provider.lower() in q:

                temp = df[
                    df["provider"] == provider
                ]

                answer = (
                    f"### 🚀 {provider}\n\n"
                    f"Launches: **{len(temp):,}**\n\n"
                    f"Rocket Types: **{temp['rocket'].nunique()}**\n\n"
                    f"Mission Types: **{temp['mission_type'].nunique()}**\n\n"
                    f"Years Active: **{temp['year'].min()}–{temp['year'].max()}**"
                )

                found = True

                break

        if not found:

            for rocket in df["rocket"].dropna().unique():

                if rocket.lower() in q:

                    temp = df[
                        df["rocket"] == rocket
                    ]

                    answer = (
                        f"### 🛰 {rocket}\n\n"
                        f"Launches: **{len(temp):,}**\n\n"
                        f"Providers: **{temp['provider'].nunique()}**\n\n"
                        f"Mission Types: **{temp['mission_type'].nunique()}**"
                    )

                    found = True

                    break

        if not found:

            answer = (
                "🤔 I couldn't answer that yet.\n\n"
                "Try asking:\n\n"
                "- Which provider has the most launches?\n"
                "- What is the most used rocket?\n"
                "- Which year had the most launches?\n"
                "- Tell me about SpaceX\n"
                "- Tell me about Falcon 9"
            )

    st.divider()

    st.markdown("## 🤖 Copilot Response")

    st.markdown(answer)