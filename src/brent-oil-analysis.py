import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.stattools import adfuller, acf, pacf

# Load Brent Oil Price Dataset
def load_data(file_path):
    """Loads the Brent oil price dataset."""
    df = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
    df.sort_index(inplace=True)  # Ensure data is sorted by date
    return df

# Visualizing Data Trends
def plot_trends(df):
    """Plots the oil price trend over time."""
    plt.figure(figsize=(12, 5))
    plt.plot(df, label='Brent Oil Price', color='blue')
    plt.title('Brent Oil Price Trends')
    plt.xlabel('Year')
    plt.ylabel('Price (USD per Barrel)')
    plt.legend()
    plt.grid()
    plt.show()

# Check for Missing Values
def check_missing_values(df):
    """Checks for missing values in the dataset."""
    missing = df.isnull().sum()
    print("Missing Values:\n", missing)

# Perform Stationarity Test (ADF Test)
def adf_test(series):
    """Runs the Augmented Dickey-Fuller test for stationarity."""
    result = adfuller(series.dropna())
    print("\nAugmented Dickey-Fuller Test Results:")
    print(f"ADF Statistic: {result[0]}")
    print(f"p-value: {result[1]}")
    print("Critical Values:")
    for key, value in result[4].items():
        print(f"   {key}: {value}")
    if result[1] <= 0.05:
        print("Conclusion: The data is stationary.")
    else:
        print("Conclusion: The data is NOT stationary.")

# AutoCorrelation and Partial AutoCorrelation Analysis
def plot_acf_pacf(series, lags=40):
    """Plots ACF and PACF for time series analysis."""
    from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    plot_acf(series.dropna(), ax=axes[0], lags=lags)
    plot_pacf(series.dropna(), ax=axes[1], lags=lags)
    plt.show()

# Main Execution
def main():
    file_path = "brent_oil_prices.csv"  # Update with your actual dataset path
    df = load_data(file_path)
    print("Dataset Head:\n", df.head())
    
    # Check for missing values
    check_missing_values(df)
    
    # Plot trends
    plot_trends(df)
    
    # Perform ADF Test
    adf_test(df.iloc[:, 0])
    
    plot_acf_pacf(df.iloc[:, 0])
    
if __name__ == "__main__":
    main()
