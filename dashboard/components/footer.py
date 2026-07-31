"""
Reusable footer component.
"""

import streamlit as st


def show_footer() -> None:
    """
    Display dashboard footer.
    """

    st.divider()

    st.caption(
        "🚀 AstraPredict v2.0"
    )

    st.caption(
        "Built with FastAPI • Streamlit • Plotly • Scikit-Learn"
    )