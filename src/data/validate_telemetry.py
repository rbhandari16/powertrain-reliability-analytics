import pandas as pd

INPUT_PATH = "data/processed/power_unit_telemetry_clean.csv"


def load_data(path):
    """Load telemetry data from CSV."""
    df = pd.read_csv(path)
    return df


def check_missing_values(df):
    """Return missing-value counts and percentages."""

    missing_count = df.isna().sum()
    missing_percentage = (
        df.isna().mean() * 100
    )

    report = pd.DataFrame({
        "missing_count": missing_count,
        "missing_percentage": missing_percentage.round(3)
    })

    return report[report["missing_count"] > 0]


def check_duplicates(df):
    """Check duplicate records."""

    duplicate_count = df.duplicated().sum()
    duplicate_percentage = (
        duplicate_count / len(df) * 100
    )

    return duplicate_count, duplicate_percentage


def check_timestamp(df):
    """Validate timestamp ordering."""

    timestamps = pd.to_datetime(
        df["timestamp"],
        errors="coerce"
    )

    invalid_timestamps = timestamps.isna().sum()
    ordered = timestamps.is_monotonic_increasing

    return ordered, invalid_timestamps


def check_numeric_ranges(df):
    """Check basic telemetry limits."""

    checks = {
        "rpm_below_minimum": (df["rpm"] < 0).sum(),

        "rpm_above_maximum": (
            df["rpm"] > 15000
        ).sum(),

        "negative_torque": (
            df["torque"] < 0
        ).sum(),

        "negative_power": (
            df["power_output"] < 0
        ).sum(),

        "negative_oil_pressure": (
            df["oil_pressure"] < 0
        ).sum(),

        "negative_fuel_flow": (
            df["fuel_flow"] < 0
        ).sum(),

        "negative_battery_voltage": (
            df["battery_voltage"] < 0
        ).sum(),

        "negative_vibration": (
            df["vibration"] < 0
        ).sum(),
    }

    return checks


def print_status(label, value):
    """Print PASS/FAIL status."""

    if value == 0:
        print(f"PASS | {label}: {value}")
    else:
        print(f"FAIL | {label}: {value}")


def generate_quality_report(df):

    print("=" * 65)
    print("POWER UNIT TELEMETRY — DATA QUALITY REPORT")
    print("=" * 65)

    # ---------------------------------------------------------
    # Dataset overview
    # ---------------------------------------------------------

    print("\nDATASET OVERVIEW")
    print("-" * 65)

    print(f"Rows:    {len(df):,}")
    print(f"Columns: {len(df.columns)}")

    # ---------------------------------------------------------
    # Missing values
    # ---------------------------------------------------------

    print("\nMISSING VALUES")
    print("-" * 65)

    missing_report = check_missing_values(df)

    if missing_report.empty:

        print("PASS | No missing values detected.")

    else:

        print(missing_report)

    # ---------------------------------------------------------
    # Duplicates
    # ---------------------------------------------------------

    print("\nDUPLICATE RECORDS")
    print("-" * 65)

    duplicate_count, duplicate_percentage = (
        check_duplicates(df)
    )

    print(f"Duplicate rows: {duplicate_count:,}")
    print(
        f"Duplicate percentage: "
        f"{duplicate_percentage:.3f}%"
    )

    # ---------------------------------------------------------
    # Timestamp validation
    # ---------------------------------------------------------

    print("\nTIMESTAMP VALIDATION")
    print("-" * 65)

    ordered, invalid_timestamps = check_timestamp(df)

    print(
        f"Chronological order: "
        f"{'PASS' if ordered else 'FAIL'}"
    )

    print(
        f"Invalid timestamps: "
        f"{invalid_timestamps}"
    )

    # ---------------------------------------------------------
    # Range validation
    # ---------------------------------------------------------

    print("\nRANGE VALIDATION")
    print("-" * 65)

    range_checks = check_numeric_ranges(df)

    for check, count in range_checks.items():

        print_status(check, count)

    # ---------------------------------------------------------
    # Overall quality status
    # ---------------------------------------------------------

    total_missing = (
        df.isna().sum().sum()
    )

    total_range_errors = sum(
        range_checks.values()
    )

    print("\nOVERALL DATA QUALITY")
    print("-" * 65)

    if (
        total_missing == 0
        and duplicate_count == 0
        and ordered
        and total_range_errors == 0
    ):
        print("PASS | Dataset passed all validation checks.")

    else:
        print(
            "FAIL | Dataset requires investigation "
            "before analysis."
        )

    print("\n" + "=" * 65)


if __name__ == "__main__":

    df = load_data(INPUT_PATH)

    generate_quality_report(df)