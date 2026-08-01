from pathlib import Path

import pandas as pd

# ==================================================
# Paths
# ==================================================

RAW_DATA = Path("data/raw/Space_Corrected.csv")

OUTPUT_DIR = Path("data/processed")

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

OUTPUT_FILE = OUTPUT_DIR / "launches_features.csv"

# ==================================================
# Load Dataset
# ==================================================

print("=" * 60)
print("Loading Space_Corrected.csv...")
print("=" * 60)

df = pd.read_csv(RAW_DATA)

print(f"Original rows: {len(df):,}")

# ==================================================
# Remove Unnecessary Columns
# ==================================================

df = df.drop(
    columns=[
        "Unnamed: 0",
        "Unnamed: 0.1",
    ],
    errors="ignore",
)

# ==================================================
# Rename Columns
# ==================================================

df = df.rename(
    columns={
        "Company Name": "provider",
        "Location": "pad",
        "Datum": "launch_time",
        "Detail": "detail",
        "Status Mission": "status",
        " Rocket": "rocket_cost",
        "Status Rocket": "rocket_status",
    }
)

# ==================================================
# Clean Text Columns
# ==================================================

for column in [
    "provider",
    "pad",
    "detail",
]:

    df[column] = (
        df[column]
        .astype(str)
        .str.strip()
    )

# ==================================================
# Extract Rocket & Mission
# ==================================================

rocket_names = []
mission_names = []

for value in df["detail"]:

    value = str(value).strip()

    if "|" in value:

        rocket, mission = value.split("|", 1)

        rocket_names.append(
            rocket.strip()
        )

        mission_names.append(
            mission.strip()
        )

    else:

        rocket_names.append(value)

        mission_names.append(
            "Unknown"
        )

df["rocket"] = rocket_names

df["mission"] = mission_names

# ==================================================
# Classify Mission Type
# ==================================================

def classify_mission(name):

    text = str(name).lower()

    if "starlink" in text:
        return "Communications"

    if "oneweb" in text:
        return "Communications"

    if "ses" in text:
        return "Communications"

    if "gps" in text:
        return "Navigation"

    if "galileo" in text:
        return "Navigation"

    if "crew" in text:
        return "Crewed"

    if "dragon" in text:
        return "Crewed"

    if "cargo" in text:
        return "Cargo"

    if "crs" in text:
        return "Cargo"

    if "cygnus" in text:
        return "Cargo"

    if "nrol" in text:
        return "Military"

    if "spy" in text:
        return "Military"

    if "weather" in text:
        return "Weather"

    if "landsat" in text:
        return "Earth Observation"

    if "sentinel" in text:
        return "Earth Observation"

    if "earth" in text:
        return "Earth Observation"

    if "science" in text:
        return "Science"

    return "Unknown"


df["mission_type"] = df["mission"].apply(
    classify_mission
)

# ==================================================
# Convert Status
# ==================================================

status_map = {
    "Success": "Launch Successful",
    "Failure": "Launch Failure",
    "Partial Failure": "Partial Failure",
    "Prelaunch Failure": "Launch Failure",
}

df["status"] = (
    df["status"]
    .map(status_map)
    .fillna(df["status"])
)

# ==================================================
# Convert Date
# ==================================================

df["launch_time"] = pd.to_datetime(
    df["launch_time"],
    utc=True,
    errors="coerce",
)

df = df.dropna(
    subset=["launch_time"]
)

df["year"] = df["launch_time"].dt.year

df["month"] = df["launch_time"].dt.month

df["day"] = df["launch_time"].dt.day

df["hour"] = df["launch_time"].dt.hour

df["day_of_week"] = (
    df["launch_time"]
    .dt.day_name()
)

# ==================================================
# Remove Missing Values
# ==================================================

df = df.dropna(
    subset=[
        "provider",
        "rocket",
    ]
)

# ==================================================
# Remove Duplicates
# ==================================================

df = df.drop_duplicates(
    subset=[
        "provider",
        "rocket",
        "launch_time",
    ]
)

# ==================================================
# Sort Dataset
# ==================================================

df = df.sort_values(
    "launch_time"
)

df = df.reset_index(
    drop=True
)

# ==================================================
# Create IDs
# ==================================================

df["provider_id"] = (
    df["provider"]
    .astype("category")
    .cat.codes
)

df["rocket_id"] = (
    df["rocket"]
    .astype("category")
    .cat.codes
)

df["mission_type_id"] = (
    df["mission_type"]
    .astype("category")
    .cat.codes
)

df["pad_id"] = (
    df["pad"]
    .astype("category")
    .cat.codes
)

# ==================================================
# Mission Name
# ==================================================

df["name"] = (
    df["rocket"]
    + " | "
    + df["mission"]
)

# ==================================================
# Final Columns
# ==================================================

df = df[
    [
        "name",
        "provider",
        "rocket",
        "status",
        "launch_time",
        "pad",
        "mission_type",
        "year",
        "month",
        "day",
        "day_of_week",
        "hour",
        "provider_id",
        "rocket_id",
        "mission_type_id",
        "pad_id",
    ]
]

# ==================================================
# Save
# ==================================================

df.to_csv(
    OUTPUT_FILE,
    index=False,
)

print("\n" + "=" * 60)
print("Dataset Successfully Processed")
print("=" * 60)

print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")
print(f"Providers: {df['provider'].nunique()}")
print(f"Rockets: {df['rocket'].nunique()}")
print(f"Mission Types: {df['mission_type'].nunique()}")

print("\nSaved to:")
print(OUTPUT_FILE)

print("\nDone!")