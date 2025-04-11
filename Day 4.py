import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv(r'C:\Users\Akash\OneDrive\Desktop\python datasetproject\cleaned_villages_towns_population_dataset.csv')

# Filter STATE-level data only
df_state = df[(df['Region Type'] == 'STATE') & (df['Total/Rural/Urban'] == 'Total')]

# Select relevant columns
density_df = df_state[['Name', 'Population - Persons', 'Area (sq km)']].copy()
density_df.dropna(inplace=True)

# Convert to numeric just in case
density_df['Population - Persons'] = pd.to_numeric(density_df['Population - Persons'], errors='coerce')
density_df['Area (sq km)'] = pd.to_numeric(density_df['Area (sq km)'], errors='coerce')

# Calculate population density
density_df['Population Density'] = (density_df['Population - Persons'] / density_df['Area (sq km)']).round(2)

# Sort
top_dense = density_df.sort_values(by='Population Density', ascending=False).head(10)
bottom_dense = density_df.sort_values(by='Population Density', ascending=True).head(10)

# --- Plot Top 10 Densely Populated States ---
plt.figure(figsize=(12, 6))
plt.bar(top_dense['Name'], top_dense['Population Density'], color='crimson')
plt.title('Top 10 Most Densely Populated States')
plt.ylabel('People per sq km')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# --- Plot Bottom 10 Sparsely Populated States ---
plt.figure(figsize=(12, 6))
plt.bar(bottom_dense['Name'], bottom_dense['Population Density'], color='teal')
plt.title('Top 10 Least Densely Populated States')
plt.ylabel('People per sq km')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# --- Print Tables for Reference ---
print("\n📊 Most Densely Populated States:")
print(top_dense[['Name', 'Population Density']])

print("\n📉 Least Densely Populated States:")
print(bottom_dense[['Name', 'Population Density']])
