import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv(r'C:\Users\Akash\OneDrive\Desktop\python datasetproject\cleaned_villages_towns_population_dataset.csv')

# Filter only STATE-level entries to avoid district-level duplicates
df_state = df[df['Region Type'] == 'STATE']

# Select necessary columns
gender_data = df_state[['Total/Rural/Urban', 'Population - Males', 'Population - Females']].copy()

# Drop missing values
gender_data.dropna(inplace=True)

# Calculate Sex Ratio: Females per 1000 Males
gender_data['Sex Ratio'] = (gender_data['Population - Females'] / gender_data['Population - Males']) * 1000

# Group by category (Total, Rural, Urban) and calculate average sex ratio
avg_sex_ratio = gender_data.groupby('Total/Rural/Urban')['Sex Ratio'].mean().round(2).reset_index()

# Print result
print("📊 Average Sex Ratio (Females per 1000 Males):")
print(avg_sex_ratio)

# Plotting
plt.figure(figsize=(8, 5))
plt.bar(avg_sex_ratio['Total/Rural/Urban'], avg_sex_ratio['Sex Ratio'], color=['seagreen', 'skyblue', 'salmon'])
plt.title('Average Sex Ratio by Region Type (Females per 1000 Males)')
plt.ylabel('Sex Ratio')
plt.ylim(880, 960)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
