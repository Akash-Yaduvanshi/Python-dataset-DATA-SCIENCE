import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv(r'C:\Users\Akash\OneDrive\Desktop\python datasetproject\cleaned_villages_towns_population_dataset.csv')

# Filter only "STATE" level and "Total" category
df_state = df[(df['Region Type'] == 'STATE') & (df['Total/Rural/Urban'] == 'Total')]

# Group by state name and sum the population
state_population = df_state[['Name', 'Population - Persons']].copy()
state_population.columns = ['State', 'Total Population']

# Drop NaN values and ensure numeric
state_population.dropna(inplace=True)
state_population['Total Population'] = pd.to_numeric(state_population['Total Population'], errors='coerce')

# Sort
top_states = state_population.sort_values(by='Total Population', ascending=False).head(10)
bottom_states = state_population.sort_values(by='Total Population', ascending=True).head(10)

# Plot Top 10
plt.figure(figsize=(12, 6))
plt.bar(top_states['State'], top_states['Total Population'], color='royalblue')
plt.title('Top 10 Most Populous States in India')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Population')
plt.tight_layout()
plt.show()

# Plot Bottom 10
plt.figure(figsize=(12, 6))
plt.bar(bottom_states['State'], bottom_states['Total Population'], color='tomato')
plt.title('Bottom 10 Least Populous States in India')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Population')
plt.tight_layout()
plt.show()
