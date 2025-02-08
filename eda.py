import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Crime_Data_from_2020_to_Present.csv')

# Convert date columns to datetime
df['DATE OCC'] = pd.to_datetime(df['DATE OCC'])
df['Year-Month'] = df['DATE OCC'].dt.to_period('M')

# Plot overall crime trends
crime_counts = df.groupby('Year-Month').size()
plt.figure(figsize=(12, 6))
crime_counts.plot(kind='line', marker='o')
plt.title('Overall Crime Trends from 2020 to Present')
plt.xlabel('Year-Month')
plt.ylabel('Number of Crimes')
plt.grid(True)
plt.show()
