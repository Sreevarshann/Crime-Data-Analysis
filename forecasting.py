from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Crime_Data_from_2020_to_Present.csv')
df['DATE OCC'] = pd.to_datetime(df['DATE OCC'])
df['Year-Month'] = df['DATE OCC'].dt.to_period('M')

# Count crimes per month
crime_counts = df['Year-Month'].value_counts().sort_index()
crime_counts.index = crime_counts.index.to_timestamp()

# Fit ARIMA model
model = ARIMA(crime_counts, order=(5,1,0))
model_fit = model.fit()

# Forecast next 24 months
forecast = model_fit.forecast(steps=24)

plt.figure(figsize=(10, 6))
plt.plot(crime_counts, label='Original Data')
plt.plot(forecast, label='Forecasted Data', linestyle='--')
plt.title('Crime Rate Forecast')
plt.xlabel('Year-Month')
plt.ylabel('Number of Crimes')
plt.legend()
plt.xticks(rotation=45)
plt.show()
