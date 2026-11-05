"""
EXPERIMENT 2
Title: PERFORM EXPLORATORY DATA ANALYSIS (EDA) ON WITH DATASETS LIKE EMAIL DATA SET
Aim: To Perform EDA on dataset using packages and get insights from data.
Procedure:
  1. Import the dataset
  2. View the head of the data
  3. View the basic information of data and description of data
  4. Find the unique value of data and verify the duplication of data
  5. Plot a graph for unique value of dataset
  6. Verify the presence of null value and replace the null value
  7. Visualize the needed data
Dataset: emails.csv (columns: 'text', 'spam')
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# File path resolution: looks for emails.csv in current directory or user downloads
file_candidates = [
    'emails.csv',
    'C:/Users/smily/Downloads/emails.csv',
    os.path.expanduser('~/Downloads/emails.csv'),
    '/home/shaber/Downloads/emails.csv'
]

file_path = None
for p in file_candidates:
    if os.path.exists(p):
        file_path = p
        break

if file_path:
    print(f"Loading dataset from: {file_path}")
    df = pd.read_csv(file_path)
else:
    print("Warning: 'emails.csv' not found locally. Generating synthetic sample dataset for demonstration...")
    import numpy as np
    np.random.seed(42)
    sample_texts = [
        "Subject: naturally irresistible your corporate identity...",
        "Subject: the stock trading gunslinger fanny is here...",
        "Subject: unbelievable new homes made easy inside...",
        "Subject: 4 color printing special request deal...",
        "Subject: meeting scheduled for tomorrow morning..."
    ] * 200
    df = pd.DataFrame({
        'text': sample_texts,
        'spam': np.random.choice([0, 1], size=len(sample_texts), p=[0.76, 0.24])
    })

# 1. Display the first few rows
print("\n--- First 5 Rows (Head) ---")
print(df.head())

# 2. Basic dataset information
print("\n--- Dataset Info ---")
print(df.info())

# 3. Descriptive statistics
print("\n--- Descriptive Statistics ---")
print(df.describe())

# 4. Check for missing values
print("\n--- Missing Values Count ---")
print(df.isnull().sum())

# 5. Feature Engineering: Email length calculation
df['email_length'] = df['text'].apply(len)
print("\n--- DataFrame with 'email_length' ---")
print(df.head())

# 6. Plot the distribution of email lengths
plt.figure(figsize=(10, 6))
sns.histplot(df['email_length'], bins=50, kde=True, color='purple')
plt.title('Distribution of Email Lengths')
plt.xlabel('Email Length')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 7. Count emails by category and plot
category_counts = df['spam'].value_counts()
print("\n--- Spam Category Counts ---")
print(category_counts)

plt.figure(figsize=(10, 6))
category_counts.plot(kind='bar', color=['skyblue', 'salmon'])
plt.title('Email Categories')
plt.xlabel('Category (0 = Legitimate, 1 = Spam)')
plt.ylabel('Number of Emails')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

print("\nResult: Thus, the program to perform exploratory data analysis (EDA) on with datasets like email data set was executed.")
