import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.vector_ar.var_model import VAR
from arch import arch_model
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Load Data
df = pd.read_csv("brent_oil_prices.csv", parse_dates=["Date"], index_col="Date")
df = df.sort_index()

# Exploratory Data Analysis
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x=df.index, y="Price")
plt.title("Brent Oil Prices Over Time")
plt.xlabel("Year")
plt.ylabel("Price (USD per barrel)")
plt.show()

# Differencing for Stationarity
df['Price_diff'] = df['Price'].diff().dropna()

# ARIMA Model
arima_model = ARIMA(df['Price'].dropna(), order=(2,1,2))
arima_result = arima_model.fit()
print(arima_result.summary())

# GARCH Model
garch_model = arch_model(df['Price_diff'].dropna(), vol='Garch', p=1, q=1)
garch_result = garch_model.fit()
print(garch_result.summary())

# VAR Model (for multivariate analysis with GDP, Inflation, etc.)
# Assuming external data is included in df
df_var = df[['Price', 'GDP', 'Inflation']].dropna()
var_model = VAR(df_var)
var_result = var_model.fit()
print(var_result.summary())

# LSTM Model
scaler = MinMaxScaler()
df['Price_scaled'] = scaler.fit_transform(df[['Price']])
X, y = [], []
n_steps = 10  # Time steps for LSTM
for i in range(n_steps, len(df)):
    X.append(df['Price_scaled'].values[i-n_steps:i])
    y.append(df['Price_scaled'].values[i])
X, y = np.array(X), np.array(y)
X = X.reshape((X.shape[0], X.shape[1], 1))

# LSTM Model Architecture
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(n_steps, 1)),
    LSTM(50, return_sequences=False),
    Dense(25),
    Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X, y, epochs=20, batch_size=16)

# Predictions
predicted_prices = model.predict(X)
predicted_prices = scaler.inverse_transform(predicted_prices)

# Visualization
plt.figure(figsize=(12, 6))
plt.plot(df.index[n_steps:], df['Price'][n_steps:], label='Actual Price')
plt.plot(df.index[n_steps:], predicted_prices, label='Predicted Price', linestyle='dashed')
plt.title('Brent Oil Price Prediction using LSTM')
plt.xlabel('Year')
plt.ylabel('Price (USD per barrel)')
plt.legend()
plt.show()
