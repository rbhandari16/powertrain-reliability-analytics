import pandas as pd


INPUT_PATH = "data/raw/power_unit_telemetry_corrupted.csv"


def load_data(path):
    """Load telemetry data from CSV."""
    return pd.read_csv(path)


def check_missing_values(df):
    """Check for missing values."""
    missing = df.isna().sum()

    return missing[missing > 0]


def check_duplicates(df):
    """Check for duplicate rows."""
    return df.duplicated().sum()


def check_timestamp_order(df):
    """Check whether timestamps are ordered."""
    timestamps = pd.to_datetime(df["timestamp"])

    return timestamps.is_monotonic_increasing


def check_numeric_ranges(df):
    """Check telemetry values against basic physical limits."""

    checks = {
        "rpm_below_minimum": (df["rpm"] < 0).sum(),
        "rpm_above_maximum": (df["rpm"] > 15000).sum(),
        "negative_torque": (df["torque"] < 0).sum(),
        "negative_power": (df["power_output"] < 0).sum(),
        "negative_oil_pressure": (df["oil_pressure"] < 0).sum(),
        "negative_fuel_flow": (df["fuel_flow"] < 0).sum(),
        "negative_battery_voltage": (df["battery_voltage"] < 0).sum(),
        "negative_vibration": (df["vibration"] < 0).sum(),
    }

    return checks


def generate_quality_report(df):
    """Generate a basic data-quality report."""

    print("=" * 60)
    print("POWER UNIT TELEMETRY — DATA QUALITY REPORT")
    print("=" * 60)

    print("\nDataset shape:")
    print(df.shape)

    print("\nMissing values:")
    missing = check_missing_values(df)

    if len(missing) == 0:
        print("No missing values detected.")
    else:
        print(missing)

    print("\nDuplicate rows:")
    print(check_duplicates(df))

    print("\nTimestamp ordered:")
    print(check_timestamp_order(df))

    print("\nRange validation:")

    range_checks = check_numeric_ranges(df)

    for check, count in range_checks.items():
        status = "PASS" if count == 0 else "FAIL"
        print(f"{status:>5} | {check}: {count}")

    print("\n" + "=" * 60)


if __name__ == "__main__":

    df = load_data(INPUT_PATH)

    generate_quality_report(df)