import joblib
import pandas as pd

from fastapi import FastAPI

from api.schemas import LaunchRequest
from src.config import MODEL_DIR

app = FastAPI(
    title="AstraPredict API",
    version="1.0.0",
)

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