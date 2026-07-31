import joblib
import pandas as pd

from datetime import datetime
from fastapi import FastAPI, HTTPException

from api.schemas import LaunchRequest
from src.config import MODEL_DIR
from src.live_launches import get_next_launch

app = FastAPI(
    title="AstraPredict API",
    version="1.2.0",
)

# Load trained ML model once at startup
model = joblib.load(
    MODEL_DIR / "launch_success_model.joblib"
)


@app.get("/")
def home():
    return {
        "message": "🚀 Welcome to AstraPredict API!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": True,
    }


@app.post("/predict")
def predict(request: LaunchRequest):
    """
    Predict whether a launch will succeed.
    """

    data = pd.DataFrame(
        [
            {
                "provider": request.provider,
                "rocket": request.rocket,
                "mission_type": request.mission_type,
                "pad": request.pad,
                "year": request.year,
                "month": request.month,
                "day": request.day,
                "hour": request.hour,
            }
        ]
    )

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    return {
        "prediction": int(prediction),
        "success_probability": round(float(probability), 4),
    }


@app.get("/next-launch")
def next_launch():
    """
    Return the next upcoming launch.
    """

    launch = get_next_launch()

    if launch is None:
        raise HTTPException(
            status_code=404,
            detail="No upcoming launches found.",
        )

    # -----------------------------------------
    # Provider
    # -----------------------------------------
    provider = "Unknown"

    if launch.get("launch_service_provider"):
        provider = launch["launch_service_provider"].get(
            "name",
            "Unknown",
        )

    # -----------------------------------------
    # Rocket
    # -----------------------------------------
    rocket = "Unknown"

    if launch.get("rocket"):
        rocket = (
            launch["rocket"]
            .get("configuration", {})
            .get("full_name", "Unknown")
        )

    # -----------------------------------------
    # Mission
    # -----------------------------------------
    mission = "Unknown"
    description = ""

    if launch.get("mission"):
        mission = launch["mission"].get(
            "type",
            "Unknown",
        )

        description = launch["mission"].get(
            "description",
            "",
        )

    # -----------------------------------------
    # Launch Pad & Coordinates
    # -----------------------------------------
    pad = "Unknown"
    location = "Unknown"

    latitude = None
    longitude = None

    if launch.get("pad"):

        pad = launch["pad"].get(
            "name",
            "Unknown",
        )

        location_data = launch["pad"].get(
            "location",
            {},
        )

        location = location_data.get(
            "name",
            "Unknown",
        )

        latitude = launch["pad"].get("latitude")
        longitude = launch["pad"].get("longitude")

    # -----------------------------------------
    # Launch Time
    # -----------------------------------------
    launch_time = datetime.fromisoformat(
        launch["window_start"].replace("Z", "+00:00")
    )

    # -----------------------------------------
    # Response
    # -----------------------------------------
    return {
        "id": launch.get("id"),
        "name": launch.get("name"),
        "provider": provider,
        "rocket": rocket,
        "mission": mission,
        "status": launch.get("status", {}).get(
            "name",
            "Unknown",
        ),
        "window_start": launch.get("window_start"),
        "pad": pad,
        "location": location,
        "latitude": latitude,
        "longitude": longitude,
        "description": description,

        # ML Features
        "year": launch_time.year,
        "month": launch_time.month,
        "day": launch_time.day,
        "hour": launch_time.hour,
    }