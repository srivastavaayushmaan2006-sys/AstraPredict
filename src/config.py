from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

API_ENDPOINTS = {
    "launch_library": "https://ll.thespacedevs.com/2.2.0/launch/?limit=100"
}
