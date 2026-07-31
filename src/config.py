from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Model directory
MODEL_DIR = PROJECT_ROOT / "models"

# API endpoints
API_ENDPOINTS = {
    "launch_library": "https://ll.thespacedevs.com/2.2.0/launch/?limit=100"
}