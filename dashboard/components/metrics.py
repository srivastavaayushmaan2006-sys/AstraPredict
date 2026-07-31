"""
Reusable metric card component for AstraPredict.
"""

from typing import Dict

import streamlit as st


def show_metrics(stats: Dict[str, int]) -> None:
    """
    Display dashboard KPI cards.

    Parameters
    ----------
    stats
        Dictionary containing dataset statistics.
    """

    cards = st.columns(4)

    cards[0].metric(
        "🚀 Launches",
        stats["launches"],
    )

    cards[1].metric(
        "🛰 Providers",
        stats["providers"],
    )

    cards[2].metric(
        "🚀 Rockets",
        stats["rockets"],
    )

    cards[3].metric(
        "🎯 Mission Types",
        stats["missions"],
    )