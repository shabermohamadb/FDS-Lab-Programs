"""
EXPERIMENT 9
Title: CASE STUDY - USE THE DIABETES DATA SET FROM PIMA INDIAN’S DIABETES
Aim: To perform Univariate analysis like Frequency, Mean, Median, Mode,
     Variance, Standard Deviation, Skewness and Kurtosis in pima Indians dataset.
Dataset: Pima2.csv
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis
import statistics

# File path resolution
file_candidates = [
    'Pima2.csv',
    'C:/Users/HP/OneDrive/Desktop/RESEARCH/Data/Pima2.csv',
    os.path.expanduser('~/Downloads/Pima2.csv'),
    '/home/shaber/Downloads/Pima2.csv'
]

file_path = None
for p in file_candidates:
    if os.path.exists(p):
        file_path = p
        break

if file_path:
    print(f"Loading Pima Indians Diabetes dataset from: {file_path}")
    df = pd.read_csv(file_path)
else:
    print("Warning: 'Pima2.csv' not found. Generating sample 300-row diabetes dataset...")
    np.random.seed(42)
    n = 300
    df = pd.DataFrame({
        'Unnamed: 0': range(1, n + 1),
        'npreg': np.random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], n, p=[0.14, 0.17, 0.14, 0.10, 0.11, 0.08, 0.07, 0.06, 0.05, 0.03, 0.02, 0.01, 0.01, 0.005, 0.005]),
        'glu': np.random.normal(123, 30, n).astype(int),
        'bp': np.random.normal(72, 12, n),
        'skin': np.random.normal(29, 11, n),
        'bmi': np.random.normal(32, 6.5, n),
        'ped': np.random.uniform(0.08, 2.3, n),
        'age': np.random.randint(21, 72, n),
        'type': np.random.choice(['pos', 'neg'], n, p=[0.34, 0.66])
    })

print('THE SHAPE OF THE DATASET IS \n', df.shape)
print('\nTHE DATA TYPES ARE :\n', df.dtypes)
print('\nTHE DESCRIPTION OF THE DATASET IS:\n', df.describe().T)

# Density plots for numerical attributes
df.plot(kind='density', subplots=True, layout=(3, 3), sharex=False, figsize=(12, 10))
plt.suptitle('Density Plots of Pima Indians Attributes', fontsize=14)
plt.tight_layout()
plt.show()

# --- Univariate Analysis: Pregnancies (npreg) ---
print('\n' + '=' * 60)
print('THE FREQUENCY OF PREGNANCIES IS:\n', df['npreg'].value_counts())
preg = np.array(df['npreg'].dropna())

print('MEAN                       :', statistics.mean(preg))
print('MEDIAN                     :', statistics.median(preg))
print('MODE                       :', statistics.multimode(preg))
print('VARIANCE                   :', statistics.variance(preg))
print('sTANDARS DEVIATION         :', statistics.stdev(preg))

if skew(preg) > 0:
    print("POSITIVE  SKEWNESS \n")
elif skew(preg) < 0:
    print("NEGATIVE  SKEWNESS \n")
else:
    print("NO  SKEWNESS \n")

print('KURTOSIS', kurtosis(preg))

# --- Univariate Analysis: Glucose (glu) ---
print('=' * 60)
print('THE FREQUENCY OF GLOCOSE IS:\n', df['glu'].value_counts())
G = np.array(df['glu'].dropna())

print('MEAN                       :', statistics.mean(G))
print('MEDIAN                     :', statistics.median(G))
print('MODE                       :', statistics.multimode(G))
print('VARIANCE                   :', statistics.variance(G))
print('sTANDARS DEVIATION         :', statistics.stdev(G))

if skew(G) > 0:
    print("POSITIVE  SKEWNESS \n")
elif skew(G) < 0:
    print("NEGATIVE  SKEWNESS \n")
else:
    print("NO  SKEWNESS \n")

print('KURTOSIS', kurtosis(G))

print("\nResult: Thus, the univariate analysis like Frequency, Mean, Median, Mode, Variance, Standard Deviation, Skewness and Kurtosis in pima Indians dataset was executed successfully.")
