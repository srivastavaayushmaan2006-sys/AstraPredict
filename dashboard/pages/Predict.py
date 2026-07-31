"""
AstraPredict - Predict Launch Success
"""

import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(
    page_title="Predict Launch",
    page_icon="🔮",
    layout="wide",
)

st.title("🔮 Launch Success Prediction")

st.markdown(
    """
Predict the probability of a successful space launch using the
trained AstraPredict machine learning model.
"""
)

st.divider()

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "history" not in st.session_state:
    st.session_state.history = []

# --------------------------------------------------
# Layout
# --------------------------------------------------

left, right = st.columns([2, 1])

with left:

    st.subheader("Launch Information")

    provider = st.text_input(
        "Launch Provider",
        placeholder="SpaceX",
    )

    rocket = st.text_input(
        "Rocket",
        placeholder="Falcon 9",
    )

    mission_type = st.text_input(
        "Mission Type",
        placeholder="Communications",
    )

    pad = st.text_input(
        "Launch Pad",
        placeholder="LC-39A",
    )

    col1, col2 = st.columns(2)

    with col1:
        year = st.number_input(
            "Year",
            min_value=1950,
            max_value=2100,
            value=2026,
        )

        month = st.number_input(
            "Month",
            min_value=1,
            max_value=12,
            value=1,
        )

    with col2:
        day = st.number_input(
            "Day",
            min_value=1,
            max_value=31,
            value=1,
        )

        hour = st.number_input(
            "Hour",
            min_value=0,
            max_value=23,
            value=12,
        )

with right:

    st.info(
        """
### Example

Provider: SpaceX

Rocket: Falcon 9

Mission: Communications

Pad: LC-39A
"""
    )

st.divider()

predict = st.button(
    "🚀 Predict Launch Success",
    use_container_width=True,
)

if predict:

    payload = {
        "provider": provider,
        "rocket": rocket,
        "mission_type": mission_type,
        "pad": pad,
        "year": int(year),
        "month": int(month),
        "day": int(day),
        "hour": int(hour),
    }

    try:

        response = requests.post(
            API_URL,
            json=payload,
            timeout=10,
        )

        response.raise_for_status()

        result = response.json()

        probability = result["success_probability"] * 100

        st.divider()

        st.subheader("Prediction Result")

        if result["prediction"] == 1:
            st.success("✅ Predicted Successful Launch")
        else:
            st.error("❌ Predicted Failed Launch")

        st.metric(
            "Success Probability",
            f"{probability:.2f}%",
        )

        st.progress(probability / 100)

        st.session_state.history.insert(
            0,
            {
                "Provider": provider,
                "Rocket": rocket,
                "Prediction": (
                    "Success"
                    if result["prediction"] == 1
                    else "Failure"
                ),
                "Probability": f"{probability:.2f}%",
            },
        )

    except requests.exceptions.ConnectionError:
        st.error(
            "Cannot connect to the FastAPI server.\n\n"
            "Start the API with:\n\n"
            "uvicorn api.app:app --reload"
        )

    except Exception as error:
        st.error(str(error))