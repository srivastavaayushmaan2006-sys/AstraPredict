print("Program started")
import json
import requests

from config import RAW_DATA_DIR, SPACEX_API


def fetch_launches():
    """
    Download all SpaceX launches.
    """

    print("Downloading launch data...")

    response = requests.get(SPACEX_API)

    response.raise_for_status()

    launches = response.json()

    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    output_file = RAW_DATA_DIR / "spacex_launches.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(launches, file, indent=4)

    print(f"Saved {len(launches)} launches.")
    print(f"Location: {output_file}")


if __name__ == "__main__":
    fetch_launches()
