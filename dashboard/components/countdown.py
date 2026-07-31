from datetime import datetime, timezone

import streamlit as st


def show_countdown(window_start):

    if not window_start:
        st.info("Launch time unavailable.")
        return

    launch_time = datetime.fromisoformat(
        window_start.replace("Z", "+00:00")
    )

    now = datetime.now(timezone.utc)

    remaining = launch_time - now

    if remaining.total_seconds() <= 0:
        st.success("🚀 Launch window has started!")
        return

    total_seconds = int(remaining.total_seconds())

    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Days", days)

    with c2:
        st.metric("Hours", hours)

    with c3:
        st.metric("Minutes", minutes)

    with c4:
        st.metric("Seconds", seconds)