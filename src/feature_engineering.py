import pandas as pd

from src.config import PROCESSED_DATA_DIR


def engineer_features():
    """
    Load the processed dataset and create
    machine-learning-friendly features.
    """

    input_file = PROCESSED_DATA_DIR / "launches.csv"

    df = pd.read_csv(input_file, parse_dates=["launch_time"])

    
    # Time-based features
    

    df["day"] = df["launch_time"].dt.day
    df["day_of_week"] = df["launch_time"].dt.day_name()
    df["hour"] = df["launch_time"].dt.hour

    
    # Simple categorical encodings
    

    df["provider_id"] = df["provider"].astype("category").cat.codes
    df["rocket_id"] = df["rocket"].astype("category").cat.codes
    df["mission_type_id"] = df["mission_type"].astype("category").cat.codes
    df["pad_id"] = df["pad"].astype("category").cat.codes

    
    # Save engineered dataset
   
    output_file = PROCESSED_DATA_DIR / "launches_features.csv"

    df.to_csv(output_file, index=False)

    print(f"\nSaved feature dataset to:\n{output_file}")

    return df


if __name__ == "__main__":

    df = engineer_features()

    print(df.head())

    print()

    print(df.info())