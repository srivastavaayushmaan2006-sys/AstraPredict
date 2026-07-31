"""
Reusable feature card component.
"""

import streamlit as st


def show_feature_card(
    title: str,
    icon: str,
    description: str,
    features: list[str],
) -> None:
    """
    Display a reusable feature card.

    Parameters
    ----------
    title
        Card title.

    icon
        Emoji displayed before the title.

    description
        Short description.

    features
        List of bullet points.
    """

    with st.container(border=True):

        st.subheader(f"{icon} {title}")

        st.write(description)

        st.markdown("### Features")

        for feature in features:
            st.write(f"✅ {feature}")