import requests
import streamlit as st

from utils import load_dataset

from components.ai_insights import show_ai_insights
from components.kpi_cards import show_kpi_cards
from components.charts import (
    launches_by_year,
    mission_type_chart,
    top_providers,
)
from components.countdown import show_countdown
from components.info_card import info_card
from components.launch_map import show_launch_map
from components.provider_stats import show_provider_stats
from components.rocket_stats import show_rocket_stats

st.set_page_config(
    page_title="Mission Control",
    page_icon="🚀",
    layout="wide",
)

API_URL = "http://127.0.0.1:8000"

# ==================================================
# Load Historical Dataset
# ==================================================

df = load_dataset()

# ==================================================
# Header
# ==================================================

st.title("🚀 Mission Control")

st.markdown(
    "Real-time launch tracking and AI-powered launch success prediction."
)

show_kpi_cards(df)

st.divider()

# ==================================================
# Load Latest Launch
# ==================================================

with st.spinner("Loading latest launch..."):

    try:

        response = requests.get(
            f"{API_URL}/next-launch",
            timeout=15,
        )

        response.raise_for_status()

        launch = response.json()

    except Exception as e:

        st.error(f"Unable to load launch.\n\n{e}")
        st.stop()

# ==================================================
# AI Prediction
# ==================================================

prediction = None

try:

    prediction_payload = {
        "provider": launch["provider"],
        "rocket": launch["rocket"],
        "mission_type": launch["mission"],
        "pad": launch["pad"],
        "year": launch["year"],
        "month": launch["month"],
        "day": launch["day"],
        "hour": launch["hour"],
    }

    prediction_response = requests.post(
        f"{API_URL}/predict",
        json=prediction_payload,
        timeout=15,
    )

    prediction_response.raise_for_status()

    prediction = prediction_response.json()

except Exception:

    prediction = None

# ==================================================
# Mission Header
# ==================================================

st.success("Latest launch loaded!")

st.subheader(launch["name"])

st.caption(
    f"Launch Window: {launch['window_start']}"
)

st.divider()

# ==================================================
# Countdown
# ==================================================

st.subheader("⏳ Launch Countdown")

show_countdown(
    launch["window_start"]
)

st.divider()

# ==================================================
# Mission Information + AI
# ==================================================

left, right = st.columns([2, 1])

# --------------------------------------------------
# Mission Information
# --------------------------------------------------

with left:

    st.subheader("🚀 Mission Information")

    row1 = st.columns(3)

    with row1[0]:
        info_card(
            "🚀 Provider",
            launch["provider"],
        )

    with row1[1]:
        info_card(
            "🛰 Rocket",
            launch["rocket"],
        )

    with row1[2]:
        info_card(
            "📡 Mission",
            launch["mission"],
        )

    row2 = st.columns(3)

    with row2[0]:
        info_card(
            "📍 Launch Pad",
            launch["pad"],
        )

    with row2[1]:
        info_card(
            "🌍 Location",
            launch["location"],
        )

    with row2[2]:
        info_card(
            "📅 Status",
            launch["status"],
        )

    st.markdown("### 📖 Mission Description")

    description = launch.get("description")

    if description:
        st.write(description)
    else:
        st.info("No mission description available.")

# --------------------------------------------------
# AI Prediction
# --------------------------------------------------

with right:

    st.subheader("🤖 AstraPredict")

    if prediction is None:

        st.warning("Prediction unavailable.")

    else:

        probability = prediction["success_probability"]

        st.metric(
            "Success Probability",
            f"{probability * 100:.1f}%"
        )

        st.progress(probability)

        if probability >= 0.90:

            st.success("🟢 Very High Confidence")

        elif probability >= 0.75:

            st.info("🔵 High Confidence")

        elif probability >= 0.60:

            st.warning("🟡 Moderate Confidence")

        else:

            st.error("🔴 Low Confidence")

        st.divider()

        if prediction["prediction"] == 1:

            st.success(
                "🚀 Predicted Outcome\n\nSUCCESS"
            )

        else:

            st.error(
                "❌ Predicted Outcome\n\nFAILURE"
            )

        # ==========================================
        # AI Mission Analysis
        # ==========================================

        st.divider()

        show_ai_insights(
            df=df,
            launch=launch,
            prediction=prediction,
        )

st.divider()

# ==================================================
# Launch Map
# ==================================================

st.subheader("🌍 Launch Site")

show_launch_map(launch)

st.divider()

# ==================================================
# Historical Intelligence
# ==================================================

st.subheader("📊 Historical Intelligence")

provider_col, rocket_col = st.columns(2)

with provider_col:

    show_provider_stats(
        df,
        launch["provider"],
    )

with rocket_col:

    show_rocket_stats(
        df,
        launch["rocket"],
    )

st.divider()

# ==================================================
# Historical Analytics
# ==================================================

st.header("📈 Historical Analytics")

chart1, chart2 = st.columns(2)

with chart1:

    launches_by_year(df)

with chart2:

    mission_type_chart(df)

st.divider()

top_providers(df)

st.divider()

# ==================================================
# Footer
# ==================================================

st.caption(
    "🚀 AstraPredict • Mission Control • Live Launch Intelligence"
)