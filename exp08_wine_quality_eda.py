"""
EXPERIMENT 8
Title: PERFORM EDA ON WINE QUALITY DATA SET
Aim: To write a python program for EDA on Wine Quality Data Set.
Procedure:
  1. Import library
  2. Import wine dataset
  3. Perform EDA to display information, description of data.
  4. Analyse the content of alcohol consumption and visualize it
Datasets: winequality-red.csv, winequality-white.csv (semicolon delimited ';')
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew

# Locate wine quality dataset files
def find_wine_file(filename):
    candidates = [
        filename,
        os.path.join('C:/Users/smily/Downloads', filename),
        os.path.expanduser(f'~/Downloads/{filename}'),
        f'/home/shaber/Downloads/{filename}'
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return None

red_path = find_wine_file('winequality-red.csv')
white_path = find_wine_file('winequality-white.csv')

if red_path:
    print(f"Loading red wine data from: {red_path}")
    df_red = pd.read_csv(red_path, delimiter=";")
else:
    print("Warning: 'winequality-red.csv' not found. Generating sample wine data...")
    import numpy as np
    np.random.seed(42)
    n = 1599
    df_red = pd.DataFrame({
        'fixed acidity': np.random.uniform(4.6, 15.9, n),
        'volatile acidity': np.random.uniform(0.12, 1.58, n),
        'citric acid': np.random.uniform(0.0, 1.0, n),
        'residual sugar': np.random.uniform(0.9, 15.5, n),
        'chlorides': np.random.uniform(0.01, 0.61, n),
        'free sulfur dioxide': np.random.uniform(1, 72, n),
        'total sulfur dioxide': np.random.uniform(6, 289, n),
        'density': np.random.uniform(0.990, 1.003, n),
        'pH': np.random.uniform(2.74, 4.01, n),
        'sulphates': np.random.uniform(0.33, 2.0, n),
        'alcohol': np.random.uniform(8.4, 14.9, n),
        'quality': np.random.choice([3, 4, 5, 6, 7, 8], n, p=[0.01, 0.03, 0.42, 0.40, 0.12, 0.02])
    })

if white_path:
    df_white = pd.read_csv(white_path, delimiter=";")
    print(f"Loaded white wine data from: {white_path}")

# 1. View Head & Slices
print("\n--- Red Wine DataFrame Head ---")
print(df_red.head())

print("\n--- Rows 100 to 110 (df_red.iloc[100:110]) ---")
print(df_red.iloc[100:110])

# 2. Inspect Data Types
print("\n--- Data Types (df_red.dtypes) ---")
print(df_red.dtypes)

# 3. Summary Statistics
print("\n--- Descriptive Statistics (df_red.describe()) ---")
print(df_red.describe())

# 4. Dataset Information
print("\n--- Dataset Info (df_red.info()) ---")
df_red.info()

# 5. Visualizations
sns.set_theme(rc={'figure.figsize': (12, 6)})

# Quality count plot
plt.figure()
sns.countplot(data=df_red, x="quality", palette="muted")
plt.title("Distribution of Wine Quality Ratings")
plt.xlabel("Quality Score")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Alcohol distribution plot
plt.figure()
sns.histplot(df_red['alcohol'], kde=True, color='crimson')
plt.title("Distribution of Alcohol Content")
plt.xlabel("Alcohol (%)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 6. Calculate Skewness
alc_skew = skew(df_red['alcohol'])
print("\n--- Alcohol Skewness ---")
print("Skewness of alcohol content:", alc_skew)

print("\nResult: Thus, the program to execute the EDA on wine dataset was executed successfully.")
