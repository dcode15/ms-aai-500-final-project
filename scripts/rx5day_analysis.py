from typing import List

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.holtwinters import ExponentialSmoothing, HoltWintersResults
import numpy as np


def main():
    combined_data: pd.DataFrame = pd.read_csv("../data/Cleaned_Data_Monthly.csv")
    combined_data["Date"] = pd.to_datetime(combined_data[["Year", "Month"]].assign(DAY=1))

    sns.lineplot(data=combined_data[combined_data["Region"] == "SEA"], x="Date", y="Rx5Day_Monthly_Smoothed")
    plt.show()

    monthly_avg_rainfall: pd.DataFrame = combined_data.groupby("Date")["Rx5Day_Monthly_Unsmoothed_Unstandardized"].mean().reset_index()
    sns.lineplot(data=monthly_avg_rainfall, x="Date", y="Rx5Day_Monthly_Unsmoothed_Unstandardized")
    plt.show()

    sns.regplot(data=monthly_avg_rainfall, x=monthly_avg_rainfall.index, y="Rx5Day_Monthly_Unsmoothed_Unstandardized")
    plt.show()

    model: ExponentialSmoothing = ExponentialSmoothing(
        monthly_avg_rainfall["Rx5Day_Monthly_Unsmoothed_Unstandardized"],
        trend="add",
        seasonal="add",
        initialization_method="estimated",
        seasonal_periods=3
    )
    fitted_model: HoltWintersResults = model.fit()

    plt.plot(monthly_avg_rainfall.index, fitted_model.fittedvalues)
    plt.show()

    forecast_periods: int = 240
    forecasted_values = fitted_model.forecast(forecast_periods)

    last_month: int = monthly_avg_rainfall.index.max()
    future_months: List[int] = np.arange(last_month + 1, last_month + forecast_periods + 1)
    forecast_index: pd.Series = pd.Series(future_months, name="Month_Index")

    plt.plot(monthly_avg_rainfall.index, fitted_model.fittedvalues)
    plt.plot(forecast_index, forecasted_values, color="red")
    plt.show()

if __name__ == "__main__":
    main()
