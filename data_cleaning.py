import pandas as pd

# Load dataset
df = pd.read_csv('Crime_Data_from_2020_to_Present.csv')

# Fill missing values
df['Mocodes'] = df['Mocodes'].fillna(0)
df['Vict Sex'] = df['Vict Sex'].fillna('NA')
df['Vict Descent'] = df['Vict Descent'].fillna('Not Available')
df['Premis Cd'] = df['Premis Cd'].fillna(0)
df['Premis Desc'] = df['Premis Desc'].fillna('Not Available')

# Drop unnecessary columns
df.drop(['Crm Cd 1', 'Crm Cd 2', 'Crm Cd 3', 'Crm Cd 4'], axis=1, inplace=True)

print("Data cleaning completed!")
