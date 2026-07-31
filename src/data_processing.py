import json

import pandas as pd

from src.config import RAW_DATA_DIR, PROCESSED_DATA_DIR


def build_dataset():

    input_file = RAW_DATA_DIR / "launch_library.json"

    with open(input_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    if isinstance(data, dict):
        launches = data["results"]
    else:
        launches = data

    records = []

    for launch in launches:

        if not isinstance(launch, dict):
            continue

        mission = launch.get("mission") or {}
        rocket = launch.get("rocket") or {}
        config = rocket.get("configuration") or {}
        provider = launch.get("launch_service_provider") or {}
        pad = launch.get("pad") or {}
        status = launch.get("status") or {}

        records.append(
            {
                "id": launch.get("id"),
                "name": launch.get("name"),
                "provider": provider.get("name"),
                "rocket": config.get("name"),
                "status": status.get("name"),
                "launch_time": launch.get("net"),
                "pad": pad.get("name"),
                "mission_type": mission.get("type"),
            }
        )

    df = pd.DataFrame(records)

    df["launch_time"] = pd.to_datetime(df["launch_time"], errors="coerce")

    df["year"] = df["launch_time"].dt.year
    df["month"] = df["launch_time"].dt.month

    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

    output_file = PROCESSED_DATA_DIR / "launches.csv"

    df.to_csv(output_file, index=False)

    print(f"\nSaved processed dataset to:\n{output_file}")

    return df


if __name__ == "__main__":

    df = build_dataset()

    print(df.head())