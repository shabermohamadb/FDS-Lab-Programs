"""
EXPERIMENT 6
Title: USE PANDAS TO EXPLORE AND ANALYZE A MOCK DATASET OF A RETAIL STORE’S WEEKLY SALES
Aim: To explore, analyze and visualize a mock retail store’s weekly sales dataset using features of pandas.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seed for reproducibility
np.random.seed(42)

# Create mock data
data = {
    "Week": pd.date_range(start="2023-01-01", periods=12, freq="W"),
    "Store_ID": np.random.choice([101, 102, 103], size=12),
    "Weekly_Sales": np.random.randint(10000, 30000, size=12),
    "Promotion": np.random.choice([0, 1], size=12),  # 1: Promotion Active, 0: No Promotion
    "Holiday_Week": np.random.choice([0, 1], size=12)
}

df = pd.DataFrame(data)

print("--- Generated Mock Data Dictionary ---")
print(data)

print("\n--- First Few Rows (df.head()) ---")
print(df.head())

print("\n--- Summary Statistics (df.describe()) ---")
print(df.describe())

print("\n--- Data Types (df.dtypes) ---")
print(df.dtypes)

print("\n--- Missing Values Count ---")
print(df.isnull().sum())

# Plot 1: Total weekly sales trend
plt.figure()
df.groupby("Week")["Weekly_Sales"].sum().plot(marker='o', figsize=(10, 5), color='royalblue')
plt.title("Total Weekly Sales Over Time")
plt.xlabel("Week")
plt.ylabel("Sales ($)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot 2: Average weekly sales by store
plt.figure()
df.groupby("Store_ID")["Weekly_Sales"].mean().plot(kind='bar', color='skyblue')
plt.title("Average Weekly Sales by Store")
plt.xlabel("Store ID")
plt.ylabel("Average Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Plot 3: Impact of promotion on sales
plt.figure()
df.groupby("Promotion")["Weekly_Sales"].mean().plot(kind='bar', color=['red', 'green'])
plt.xticks([0, 1], ['No Promotion', 'Promotion Active'], rotation=0)
plt.title("Average Sales: Promotion vs No Promotion")
plt.ylabel("Average Weekly Sales")
plt.tight_layout()
plt.show()

# Correlation Matrix & Heatmap
print("\n--- Correlation Matrix ---")
corr_matrix = df.corr(numeric_only=True)
print(corr_matrix)

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

print("\nResult: Thus, the python code was written and executed to explore, analyze and visualize a mock retail store’s weekly sales dataset using features of pandas.")
