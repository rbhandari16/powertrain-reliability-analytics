import numpy as np
import pandas as pd


RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)


def generate_telemetry(
    n_rows=500_000,
    n_test_sessions=100,
):
    """
    Generate synthetic power-unit telemetry.

    This dataset is synthetic and is created for educational
    and portfolio purposes. It does not represent proprietary
    Formula 1 or Red Bull Powertrains telemetry.
    """

    # ---------------------------------------------------------
    # 1. Timestamp
    # ---------------------------------------------------------

    timestamps = pd.date_range(
        start="2026-01-01",
        periods=n_rows,
        freq="100ms"
    )

    # ---------------------------------------------------------
    # 2. Test session
    # ---------------------------------------------------------

    test_ids = np.random.randint(
        1,
        n_test_sessions + 1,
        size=n_rows
    )

    # ---------------------------------------------------------
    # 3. Engine RPM
    # ---------------------------------------------------------

    rpm = np.random.normal(
        loc=9500,
        scale=1800,
        size=n_rows
    )

    rpm = np.clip(rpm, 3000, 15000)

    # ---------------------------------------------------------
    # 4. Torque
    # ---------------------------------------------------------

    torque = (
        420
        + 0.015 * (rpm - 9000)
        + np.random.normal(0, 25, n_rows)
    )

    # ---------------------------------------------------------
    # 5. Power output
    # ---------------------------------------------------------

    power_output = (
        torque * rpm / 9549
        + np.random.normal(0, 5, n_rows)
    )

    # ---------------------------------------------------------
    # 6. Engine temperature
    # ---------------------------------------------------------

    engine_temperature = (
        90
        + 0.0025 * rpm
        + 0.015 * torque
        + np.random.normal(0, 3, n_rows)
    )

    # ---------------------------------------------------------
    # 7. Oil temperature
    # ---------------------------------------------------------

    oil_temperature = (
        engine_temperature
        - 8
        + np.random.normal(0, 2, n_rows)
    )

    # ---------------------------------------------------------
    # 8. Oil pressure
    # ---------------------------------------------------------

    oil_pressure = (
        5.0
        - 0.00008 * (engine_temperature - 100)
        + np.random.normal(0, 0.12, n_rows)
    )

    # ---------------------------------------------------------
    # 9. Coolant temperature
    # ---------------------------------------------------------

    coolant_temperature = (
        75
        + 0.0018 * rpm
        + np.random.normal(0, 2, n_rows)
    )

    # ---------------------------------------------------------
    # 10. Fuel flow
    # ---------------------------------------------------------

    fuel_flow = (
        80
        + 0.002 * rpm
        + np.random.normal(0, 2, n_rows)
    )

    # ---------------------------------------------------------
    # 11. Battery voltage
    # ---------------------------------------------------------

    battery_voltage = (
        700
        + np.random.normal(0, 8, n_rows)
    )

    # ---------------------------------------------------------
    # 12. Battery current
    # ---------------------------------------------------------

    battery_current = (
        250
        + 0.015 * torque
        + np.random.normal(0, 15, n_rows)
    )

    # ---------------------------------------------------------
    # 13. Motor temperature
    # ---------------------------------------------------------

    motor_temperature = (
        65
        + 0.0008 * rpm
        + np.random.normal(0, 2.5, n_rows)
    )

    # ---------------------------------------------------------
    # 14. Vibration
    # ---------------------------------------------------------

    vibration = (
        0.25
        + 0.00002 * rpm
        + np.random.normal(0, 0.05, n_rows)
    )

    # ---------------------------------------------------------
    # 15. Ambient temperature
    # ---------------------------------------------------------

    ambient_temperature = np.random.normal(
        20,
        4,
        n_rows
    )

    # ---------------------------------------------------------
    # Combine everything into a DataFrame
    # ---------------------------------------------------------

    df = pd.DataFrame({
        "timestamp": timestamps,
        "test_id": test_ids,
        "rpm": rpm,
        "torque": torque,
        "power_output": power_output,
        "engine_temperature": engine_temperature,
        "oil_temperature": oil_temperature,
        "oil_pressure": oil_pressure,
        "coolant_temperature": coolant_temperature,
        "fuel_flow": fuel_flow,
        "battery_voltage": battery_voltage,
        "battery_current": battery_current,
        "motor_temperature": motor_temperature,
        "vibration": vibration,
        "ambient_temperature": ambient_temperature,
    })

    return df


# -------------------------------------------------------------
# Run the generator
# -------------------------------------------------------------

if __name__ == "__main__":

    df = generate_telemetry()

    output_path = "data/raw/power_unit_telemetry.csv"

    df.to_csv(
        output_path,
        index=False
    )

    print(f"Generated {len(df):,} telemetry records.")
    print(f"Saved to: {output_path}")

    print("\nDataset shape:")
    print(df.shape)

    print("\nDataset preview:")
    print(df.head())

    print("\nMissing values:")
    print(df.isna().sum())