import json

from src.api_clients import get_launch_library_data
from src.config import RAW_DATA_DIR


def save_raw_launch_data():

    print("Downloading launch data...")

    data = get_launch_library_data()

    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    output_file = RAW_DATA_DIR / "launch_library.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("Download complete.")
    print(f"Saved to {output_file}")


if __name__ == "__main__":
    save_raw_launch_data()
