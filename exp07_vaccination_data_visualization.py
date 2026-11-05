"""
EXPERIMENT 7
Title: USE SPATIAL DATASETS TO MAP VACCINATION RATES BY STATE WITH INTERACTIVE EFFECTS
       LIKE MOUSE ROLLOVER, TOOLTIPS, AND USER-SELECTED METRICS
Aim: To generate and visualize sample COVID-19 vaccination data for Indian states by creating
     bar charts, scatter plots, and heatmaps, in order to compare first dose, fully vaccinated,
     and booster dose rates across different regions.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Style settings
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# Indian states list
states = [
    'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh',
    'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand',
    'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
    'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab',
    'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura',
    'Uttar Pradesh', 'Uttarakhand', 'West Bengal'
]

# Regional groupings
regions = [
    'South', 'Northeast', 'Northeast', 'North', 'Central',
    'West', 'West', 'North', 'North', 'East',
    'South', 'South', 'Central', 'West', 'Northeast',
    'Northeast', 'Northeast', 'Northeast', 'East', 'North',
    'West', 'Northeast', 'South', 'South', 'Northeast',
    'North', 'North', 'East'
]

# Random vaccination data generation
np.random.seed(42)
df = pd.DataFrame({
    'state': states,
    'first_dose': np.random.uniform(40, 80, len(states)),
})
df['fully_vaccinated'] = df['first_dose'] * np.random.uniform(0.8, 0.95, len(df))
df['booster_rate'] = df['fully_vaccinated'] * np.random.uniform(0.5, 0.8, len(df))
df['region'] = regions
df = df.sort_values('first_dose', ascending=False)

print("--- Vaccination Dataset Overview (Top 5 States) ---")
print(df.head())

# --- Plot 1: Bar Comparison (Top 15 States) ---
top_states = df.head(15).melt(id_vars=['state'],
                              value_vars=['first_dose', 'fully_vaccinated'],
                              var_name='type', value_name='rate')

plt.figure(figsize=(12, 7))
sns.barplot(data=top_states, x='state', y='rate', hue='type', palette='Set2')
plt.title('First Dose vs Fully Vaccinated (Top 15 States)', fontsize=14)
plt.xlabel('State', fontsize=12)
plt.ylabel('Rate (%)', fontsize=12)
plt.xticks(rotation=60)
plt.tight_layout()
plt.show()

# --- Plot 2: Scatter Plot (First Dose vs Booster Rate) ---
plt.figure(figsize=(12, 7))
sns.scatterplot(data=df, x='first_dose', y='booster_rate',
                hue='region', s=100, palette='deep')

for x, y, label in zip(df['first_dose'], df['booster_rate'], df['state']):
    plt.text(x + 0.3, y + 0.3, label, fontsize=8)

plt.title('First Dose vs Booster Rate by Region', fontsize=14)
plt.xlabel('First Dose (%)', fontsize=12)
plt.ylabel('Booster Rate (%)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# --- Plot 3: Heatmap (Top 10 States) ---
top_10 = df.head(10).set_index('state')[['first_dose', 'fully_vaccinated', 'booster_rate']]

plt.figure(figsize=(10, 6))
sns.heatmap(top_10, annot=True, fmt='.1f', cmap='YlOrRd', linewidths=0.5,
            cbar_kws={'label': 'Vaccination Rate (%)'})
plt.title('Vaccination Rates Heatmap - Top 10 States', fontsize=14)
plt.xlabel('Vaccination Metric', fontsize=12)
plt.ylabel('State', fontsize=12)
plt.tight_layout()
plt.show()

print("\nResult: Thus, the python code was written and executed to explore, how data visualization can be used to compare vaccination progress across different states and regions in India.")
