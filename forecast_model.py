"""
forecast_model.py

Revenue forecast for the Olist E-commerce dataset using SARIMAX.

Workflow:
1. Load monthly revenue data from CSV
2. Fit SARIMAX time series model
3. Forecast next 6 months
4. Calculate MAPE on the last 12 months of training data
5. Save forecast results to CSV for use in Power BI or other tools

Expected input file: data/revenue_by_month.csv
Required columns:
    - Year        (int)
    - MonthNumber (1–12)
    - Revenue     (float)

Author: Rahim Rzayev
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

# -----------------------------
# Configuration
# -----------------------------
INPUT_PATH = os.path.join("data", "revenue_by_month.csv")
OUTPUT_PATH = os.path.join("data", "revenue_forecast_output.csv")

# Forecast horizon (months)
FORECAST_STEPS = 6


def load_and_prepare_data(path: str) -> pd.Series:
    """
    Load monthly revenue data and create a proper Date index.

    :param path: Path to CSV file with Year, MonthNumber, Revenue
    :return: Pandas Series indexed by Date with Revenue values
    """
    df = pd.read_csv(path)

    # Ensure correct ordering
    df = df.sort_values(by=["Year", "MonthNumber"])

    # Create a Date column: YYYY-MM-01
    df["Date"] = pd.to_datetime(
        df["Year"].astype(str) + "-" + df["MonthNumber"].astype(str) + "-01"
    )

    # Set Date as index and return the Revenue series
    ts = df.set_index("Date")["Revenue"].astype(float)

    return ts


def fit_sarimax(ts: pd.Series):
    """
    Fit a SARIMAX(1,1,1)(1,1,1,12) model to the time series.

    :param ts: Time series of Revenue indexed by Date
    :return: Fitted SARIMAX results object
    """
    model = SARIMAX(
        ts,
        order=(1, 1, 1),
        seasonal_order=(1, 1, 1, 12),
        enforce_stationarity=False,
        enforce_invertibility=False,
    )
    results = model.fit(disp=False)
    return results


def compute_mape(y_true: pd.Series, y_pred: pd.Series) -> float:
    """
    Compute Mean Absolute Percentage Error (MAPE).

    :param y_true: Actual values
    :param y_pred: Predicted values (aligned index)
    :return: MAPE as a float (e.g. 0.12 = 12%)
    """
    # Avoid division by zero
    mask = y_true != 0
    y_true = y_true[mask]
    y_pred = y_pred[mask]

    mape = np.mean(np.abs((y_true - y_pred) / y_true))
    return float(mape)


def generate_forecast(ts: pd.Series, steps: int = FORECAST_STEPS):
    """
    Fit SARIMAX and generate forecast with confidence intervals + MAPE.

    :param ts: Revenue time series
    :param steps: Number of months to forecast
    :return: (forecast_df, mape_value, results_object)
    """
    results = fit_sarimax(ts)

    # Forecast
    forecast_res = results.get_forecast(steps=steps)
    pred_mean = forecast_res.predicted_mean
    conf_int = forecast_res.conf_int()

    # Prepare forecast dataframe
    forecast_df = pd.DataFrame(
        {
            "ValueDate": pred_mean.index,
            "Forecast": pred_mean.values,
            "ValueLowerCI": conf_int.iloc[:, 0].values,
            "ValueUpperCI": conf_int.iloc[:, 1].values,
        }
    )

    # Calculate MAPE on the last 12 months of in-sample fitted values
    y_true = ts[-12:]
    y_pred = results.fittedvalues[-12:]
    mape_value = compute_mape(y_true, y_pred)

    return forecast_df, mape_value, results


def save_forecast(forecast_df: pd.DataFrame, mape_value: float, path: str):
    """
    Save forecast results to CSV for Power BI or other tools.

    Columns:
        - Name           (label, e.g. 'Revenue Forecast')
        - ValueDate      (date of forecast)
        - Forecast       (predicted revenue)
        - ValueLowerCI   (lower bound)
        - ValueUpperCI   (upper bound)
        - MAPE           (same value on all rows, for convenience)

    :param forecast_df: DataFrame from generate_forecast()
    :param mape_value: MAPE as float
    :param path: Output CSV path
    """
    out_df = forecast_df.copy()
    out_df.insert(0, "Name", "Revenue Forecast")
    out_df["MAPE"] = mape_value

    # Create folder if it doesn't exist
    os.makedirs(os.path.dirname(path), exist_ok=True)
    out_df.to_csv(path, index=False)
    print(f"✅ Forecast saved to: {path}")
    print(f"✅ MAPE (last 12 months): {mape_value * 100:.2f}%")


def plot_forecast(ts: pd.Series, forecast_df: pd.DataFrame):
    """
    Optional: Quick visualization for checking model.

    :param ts: Historical revenue series
    :param forecast_df: DataFrame with forecast results
    """
    plt.figure(figsize=(10, 5))

    # Historical data
    plt.plot(ts.index, ts.values, label="Historical Revenue", color="blue")

    # Forecast
    plt.plot(
        forecast_df["ValueDate"],
        forecast_df["Forecast"],
        label="Forecast",
        linestyle="--",
        color="orange",
    )

    # Confidence interval
    plt.fill_between(
        forecast_df["ValueDate"],
        forecast_df["ValueLowerCI"],
        forecast_df["ValueUpperCI"],
        alpha=0.2,
        label="Confidence Interval",
        color="orange",
    )

    plt.title("Revenue Forecast — Next 6 Months (SARIMAX)")
    plt.xlabel("Date")
    plt.ylabel("Revenue (USD)")
    plt.legend()
    plt.tight_layout()
    plt.show()


def main():
    # 1. Load data
    print(f"📥 Loading data from: {INPUT_PATH}")
    ts = load_and_prepare_data(INPUT_PATH)

    # 2. Generate forecast & MAPE
    print("📈 Fitting SARIMAX model and generating forecast...")
    forecast_df, mape_value, _ = generate_forecast(ts, steps=FORECAST_STEPS)

    # 3. Save to CSV for Power BI / other tools
    save_forecast(forecast_df, mape_value, OUTPUT_PATH)

    # 4. Optional: show plot (uncomment if you want a local chart)
    # plot_forecast(ts, forecast_df)


if __name__ == "__main__":
    main()
