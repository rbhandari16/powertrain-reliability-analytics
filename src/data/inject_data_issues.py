import pandas as pd
import numpy as np


INPUT_PATH = "data/raw/power_unit_telemetry.csv"
OUTPUT_PATH = "data/raw/power_unit_telemetry_corrupted.csv"


def inject_data_issues(df):

    np.random.seed(42)

    # --------------------------------------------------
    # 1. Missing values
    # --------------------------------------------------

    missing_indices = np.random.choice(
        df.index,
        size=1000,
        replace=False
    )

    df.loc[missing_indices, "oil_pressure"] = np.nan

    # --------------------------------------------------
    # 2. Sensor dropout
    # --------------------------------------------------

    dropout_start = 200000
    dropout_end = 200500

    df.loc[
        dropout_start:dropout_end,
        "battery_voltage"
    ] = np.nan

    # --------------------------------------------------
    # 3. Invalid RPM readings
    # --------------------------------------------------

    invalid_indices = np.random.choice(
        df.index,
        size=100,
        replace=False
    )

    df.loc[
        invalid_indices,
        "rpm"
    ] = 18000

    # --------------------------------------------------
    # 4. Negative pressure readings
    # --------------------------------------------------

    pressure_indices = np.random.choice(
        df.index,
        size=50,
        replace=False
    )

    df.loc[
        pressure_indices,
        "oil_pressure"
    ] = -2

    # --------------------------------------------------
    # 5. Duplicate rows
    # --------------------------------------------------

    duplicates = df.sample(
        n=200,
        random_state=42
    )

    df = pd.concat(
        [df, duplicates],
        ignore_index=True
    )

    return df


if __name__ == "__main__":

    df = pd.read_csv(INPUT_PATH)

    corrupted_df = inject_data_issues(df)

    corrupted_df.to_csv(
        OUTPUT_PATH,
        index=False
    )

    print(
        f"Created corrupted dataset with "
        f"{len(corrupted_df):,} rows."
    )

    print(
        f"Saved to: {OUTPUT_PATH}"
    )