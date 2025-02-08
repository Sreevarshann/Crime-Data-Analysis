import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv('Crime_Data_from_2020_to_Present.csv')

# Convert dates
df['DATE OCC'] = pd.to_datetime(df['DATE OCC'])

# Plot Crime Trends by Region
crime_by_area = df['AREA NAME'].value_counts()
plt.figure(figsize=(12, 6))
crime_by_area.plot(kind='bar', color='blue')
plt.title('Crime Rates by Region')
plt.xlabel('Area Name')
plt.ylabel('Number of Crimes')
plt.xticks(rotation=45)
plt.show()

# Plot Most Common Crime Types
crime_counts = df['Crm Cd Desc'].value_counts()
top_10_crimes = crime_counts.head(10)

plt.figure(figsize=(10, 7))
top_10_crimes.plot(kind='bar', color='red')
plt.title('Top 10 Most Common Crimes')
plt.xlabel('Crime Type')
plt.ylabel('Number of Crimes')
plt.xticks(rotation=45)
plt.show()
