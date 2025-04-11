import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r'C:\Users\Akash\OneDrive\Desktop\python datasetproject\cleaned_villages_towns_population_dataset.csv')

# Filter only STATE-level data and TOTAL category
df_state = df[(df['Region Type'] == 'STATE') & (df['Total/Rural/Urban'] == 'Total')]

# Select relevant columns
village_town_df = df_state[['Name', 
                            'Number of Villages (Inhabited)', 
                            'Number of Villages (Uninhabited)', 
                            'Number of Towns']].copy()

# Rename columns for clarity
village_town_df.columns = ['State', 'Inhabited Villages', 'Uninhabited Villages', 'Total Towns']

# Handle missing data
village_town_df.fillna(0, inplace=True)
village_town_df.iloc[:, 1:] = village_town_df.iloc[:, 1:].astype(int)

# Calculate total villages
village_town_df['Total Villages'] = village_town_df['Inhabited Villages'] + village_town_df['Uninhabited Villages']

# --- Plot: Top 10 States by Total Villages ---
top_village_states = village_town_df.sort_values(by='Total Villages', ascending=False).head(10)

plt.figure(figsize=(12, 6))
plt.bar(top_village_states['State'], top_village_states['Total Villages'], color='olive')
plt.title('Top 10 States by Total Number of Villages')
plt.ylabel('Number of Villages')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# --- Plot: Top 10 States by Total Towns ---
top_town_states = village_town_df.sort_values(by='Total Towns', ascending=False).head(10)

plt.figure(figsize=(12, 6))
plt.bar(top_town_states['State'], top_town_states['Total Towns'], color='steelblue')
plt.title('Top 10 States by Total Number of Towns')
plt.ylabel('Number of Towns')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# --- Print Summary Tables ---
print("\n📊 Village Distribution (Top 10 States by Total Villages):")
print(top_village_states[['State', 'Inhabited Villages', 'Uninhabited Villages', 'Total Villages']])

print("\n🏙️ Town Distribution (Top 10 States by Total Towns):")
print(top_town_states[['State', 'Total Towns']])
