import requests
import streamlit as st

st.set_page_config(
    page_title="AstraPredict",
    page_icon="🚀",
    layout="wide",
)

st.title("🚀 AstraPredict")

st.markdown(
    """
Predict the probability of a successful space launch
using our machine learning model.
"""
)

st.divider()

provider = st.text_input("Launch Provider", "SpaceX")

rocket = st.text_input("Rocket", "Falcon 9")

mission = st.text_input("Mission Type", "Communications")

pad = st.text_input("Launch Pad", "Launch Complex 39A")

col1, col2, col3, col4 = st.columns(4)

with col1:
    year = st.number_input(
        "Year",
        value=2026,
        step=1,
    )

with col2:
    month = st.number_input(
        "Month",
        value=9,
        min_value=1,
        max_value=12,
    )

with col3:
    day = st.number_input(
        "Day",
        value=18,
        min_value=1,
        max_value=31,
    )

with col4:
    hour = st.number_input(
        "Hour",
        value=14,
        min_value=0,
        max_value=23,
    )

st.divider()

if st.button("Predict Launch Success", use_container_width=True):

    payload = {
        "provider": provider,
        "rocket": rocket,
        "mission_type": mission,
        "pad": pad,
        "year": int(year),
        "month": int(month),
        "day": int(day),
        "hour": int(hour),
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload,
            timeout=10,
        )

        response.raise_for_status()

        result = response.json()

        probability = result["success_probability"] * 100

        if result["prediction"] == 1:
            st.success(
                f"✅ Predicted Successful Launch\n\n"
                f"Confidence: {probability:.1f}%"
            )
        else:
            st.error(
                f"❌ Predicted Unsuccessful Launch\n\n"
                f"Confidence: {probability:.1f}%"
            )

    except Exception as e:
        st.error(f"API Error:\n\n{e}")