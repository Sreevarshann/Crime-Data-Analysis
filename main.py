import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA

# Load Dataset
df = pd.read_csv('Crime_Data_from_2020_to_Present.csv')

# Data Cleaning
df['Mocodes'] = df['Mocodes'].fillna(0)
df['Vict Sex'] = df['Vict Sex'].fillna('NA')
df['Vict Descent'] = df['Vict Descent'].fillna('Not Available')
df['Premis Cd'] = df['Premis Cd'].fillna(0)
df['Premis Desc'] = df['Premis Desc'].fillna('Not Available')
df.drop(['Crm Cd 1', 'Crm Cd 2', 'Crm Cd 3', 'Crm Cd 4'], axis=1, inplace=True)

print("Data Cleaning Completed!")

# Convert dates to datetime format
df['DATE OCC'] = pd.to_datetime(df['DATE OCC'])
df['Year-Month'] = df['DATE OCC'].dt.to_period('M')

# EDA: Crime Trends Over Time
crime_counts = df.groupby('Year-Month').size()
plt.figure(figsize=(12, 6))
crime_counts.plot(kind='line', marker='o')
plt.title('Overall Crime Trends from 2020 to Present')
plt.xlabel('Year-Month')
plt.ylabel('Number of Crimes')
plt.grid(True)
plt.show()

# Forecasting: ARIMA Model for Crime Prediction
crime_counts.index = crime_counts.index.to_timestamp()
model = ARIMA(crime_counts, order=(5,1,0))
model_fit = model.fit()
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
