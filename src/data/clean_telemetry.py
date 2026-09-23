import pandas as pd


INPUT_PATH = "data/raw/power_unit_telemetry_corrupted.csv"
OUTPUT_PATH = "data/processed/power_unit_telemetry_clean.csv"


def clean_telemetry(df):

    original_rows = len(df)

    # ---------------------------------------------------------
    # 1. Convert timestamp
    # ---------------------------------------------------------

    df["timestamp"] = pd.to_datetime(
        df["timestamp"],
        errors="coerce"
    )

    # ---------------------------------------------------------
    # 2. Remove exact duplicate records
    # ---------------------------------------------------------

    df = df.drop_duplicates()

    # ---------------------------------------------------------
    # 3. Remove physically impossible RPM readings
    # ---------------------------------------------------------

    df.loc[
        (df["rpm"] < 0) |
        (df["rpm"] > 15000),
        "rpm"
    ] = pd.NA

    # ---------------------------------------------------------
    # 4. Remove physically impossible oil pressure
    # ---------------------------------------------------------

    df.loc[
        df["oil_pressure"] < 0,
        "oil_pressure"
    ] = pd.NA

    # ---------------------------------------------------------
    # 5. Sort chronologically
    # ---------------------------------------------------------

    df = df.sort_values(
        by=["timestamp", "test_id"]
    )

    # ---------------------------------------------------------
    # 6. Reset index
    # ---------------------------------------------------------

    df = df.reset_index(drop=True)

    cleaned_rows = len(df)

    print("\nCLEANING SUMMARY")
    print("=" * 60)

    print(
        f"Original rows: {original_rows:,}"
    )

    print(
        f"Rows after cleaning: {cleaned_rows:,}"
    )

    print(
        f"Rows removed: "
        f"{original_rows - cleaned_rows:,}"
    )

    print(
        f"Rows retained: "
        f"{cleaned_rows / original_rows * 100:.2f}%"
    )

    print("=" * 60)

    return df


if __name__ == "__main__":

    df = pd.read_csv(INPUT_PATH)

    cleaned_df = clean_telemetry(df)

    cleaned_df.to_csv(
        OUTPUT_PATH,
        index=False
    )

    print(
        f"\nClean dataset saved to:"
        f"\n{OUTPUT_PATH}"
    )