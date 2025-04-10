import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file (update path if needed)
df = pd.read_csv(r'C:\Users\Akash\OneDrive\Desktop\python datasetproject\cleaned_villages_towns_population_dataset.csv')

# Filter only STATE-level entries to avoid duplication from districts
df_state = df[df['Region Type'] == 'STATE']

# Keep only relevant columns
columns_needed = ['Total/Rural/Urban', 'Population - Persons', 'Number of Households', 'Area (sq km)']
urban_rural = df_state[columns_needed].copy()

# Drop missing data
urban_rural.dropna(inplace=True)

# Group by Rural/Urban/Total
summary = urban_rural.groupby('Total/Rural/Urban').agg({
    'Population - Persons': 'sum',
    'Number of Households': 'sum',
    'Area (sq km)': 'sum'
}).reset_index()

# Calculate population density
summary['Population Density'] = (summary['Population - Persons'] / summary['Area (sq km)']).round(2)

# Display the summary table
print("\n📊 Urban vs Rural Demographic Summary:")
print(summary)

# Plotting - Population, Households, and Density
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

# Plot 1: Population
axs[0].bar(summary['Total/Rural/Urban'], summary['Population - Persons'], color='steelblue')
axs[0].set_title('Population')
axs[0].set_ylabel('Persons')

# Plot 2: Households
axs[1].bar(summary['Total/Rural/Urban'], summary['Number of Households'], color='green')
axs[1].set_title('Number of Households')

# Plot 3: Population Density
axs[2].bar(summary['Total/Rural/Urban'], summary['Population Density'], color='tomato')
axs[2].set_title('Population Density (per sq km)')

# Layout and display
plt.suptitle('Urban vs Rural Demographics in India', fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
