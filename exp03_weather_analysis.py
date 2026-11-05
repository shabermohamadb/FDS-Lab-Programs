"""
EXPERIMENT 3
Title: USE NUMPY ARRAYS TO COMPUTE STATISTICS AND MANIPULATE NUMERICAL WEATHER DATA
Aim: To write a program to work with Numpy for performing statistical analysis on weather data.
Dataset: weather_2012.csv
"""

import os
import numpy as np
import pandas as pd

# File path resolution
file_candidates = [
    'weather_2012.csv',
    'C:/Users/smily/Downloads/weather_2012.csv',
    os.path.expanduser('~/Downloads/weather_2012.csv'),
    '/home/shaber/Downloads/weather_2012.csv'
]

file_path = None
for p in file_candidates:
    if os.path.exists(p):
        file_path = p
        break

if file_path:
    print(f"Loading weather dataset from: {file_path}")
    df = pd.read_csv(file_path, parse_dates=['Date/Time'])
else:
    print("Warning: 'weather_2012.csv' not found locally. Generating synthetic weather data...")
    dates = pd.date_range(start="2012-01-01", periods=1000, freq="h")
    df = pd.DataFrame({
        'Date/Time': dates,
        'Temp (C)': np.random.uniform(-15, 30, len(dates)),
        'Dew Point Temp (C)': np.random.uniform(-18, 20, len(dates)),
        'Rel Hum (%)': np.random.randint(40, 100, len(dates)),
        'Wind Spd (km/h)': np.random.uniform(0, 50, len(dates)),
        'Visibility (km)': np.random.choice([4.0, 8.0, 16.0, 25.0], len(dates)),
        'Weather': np.random.choice(['Clear', 'Mainly Clear', 'Mostly Cloudy', 'Cloudy', 'Snow'], len(dates))
    })

print("\n--- Weather DataFrame Head ---")
print(df.head())

# Convert columns to numpy arrays
temps = df['Temp (C)'].to_numpy()
winds = df['Wind Spd (km/h)'].to_numpy()
vis = df['Visibility (km)'].to_numpy()

# Summary statistics using NumPy
print("\n--- Temperature Statistics (NumPy) ---")
print("Temp → mean:", np.nanmean(temps), "min:", np.nanmin(temps), "max:", np.nanmax(temps), "std:", np.nanstd(temps))

print("\n--- Wind Speed Statistics (NumPy) ---")
print("Wind Speed → mean:", np.nanmean(winds), "max:", np.nanmax(winds))

# Weather condition filters
num_cloudy = np.sum(df['Weather'] == 'Cloudy')
print("\nCloudy hours:", num_cloudy)

mask = (winds > 35) & (vis == 25)
print("Extreme windy & clear-vis hours:", np.sum(mask))

# Monthly Pivot Table
df['Month'] = df['Date/Time'].dt.month
pivot = df.pivot_table(index='Month', values='Temp (C)', aggfunc=['mean', 'min', 'max', 'count'])
print("\n--- Monthly Temperature Pivot Table ---")
print(pivot)

# Grouped weather conditions
grouped = df.groupby('Weather')['Temp (C)'].agg(['mean', 'std', 'count'])
print("\n--- Top Weather Types by Count ---")
print(grouped.sort_values('count', ascending=False).head())

print("\nResult: Thus, the program to perform statistical analysis on weather data using Numpy arrays were executed.")
