"""
EXPERIMENT 4
Title: DATA CLEANING ON MESSY CUSTOMER FEEDBACK DATA USING PYTHON
Aim: To explore various variable and column filters for cleaning messy customer feedback data.
Note: In the original FDS lab syllabus, this experiment is written in R.
      This file provides the complete, idiomatic Python implementation.
      The original R script is also available in: exp4_customer_feedback_cleaning.R
"""

import numpy as np
import pandas as pd

# Step 1: Create initial messy dataframe
feedback_df = pd.DataFrame({
    'CustomerID': [101, 102, 103, np.nan, 105, 106],
    'Feedback': ["Good service", "bad Service!!", np.nan, "  excellent!! ", "Average ", ""],
    'Rating': [5, 1, np.nan, 5, 3, 2],
    'Gender': ["Male", "Female", "F", "female", "MALE", "M"]
})

print("=" * 60)
print("STEP 1: Original Raw Messy Customer Feedback Data")
print("=" * 60)
print(feedback_df)

# Step 2: Rename CustomerID to Customer_ID
feedback_df = feedback_df.rename(columns={'CustomerID': 'Customer_ID'})

# Step 3: Text cleaning (trim spaces, sentence case, remove punctuation)
feedback_df['Feedback'] = feedback_df['Feedback'].astype(str).str.strip()
feedback_df['Feedback'] = feedback_df['Feedback'].apply(lambda x: x.capitalize() if x and x != 'nan' else np.nan)
feedback_df['Feedback'] = feedback_df['Feedback'].str.replace(r'[^a-zA-Z0-9\\s]', '', regex=True)

# Step 4: Standardize and normalize Gender column
def normalize_gender(val):
    if pd.isna(val):
        return 'Other'
    v = str(val).strip().lower()
    if v in ['male', 'm']:
        return 'Male'
    elif v in ['female', 'f']:
        return 'Female'
    return 'Other'

feedback_df['Gender'] = feedback_df['Gender'].apply(normalize_gender)

print("\n" + "=" * 60)
print("STEP 2-4: Renamed, Cleaned Feedback Text & Standardized Gender")
print("=" * 60)
print(feedback_df)

# Step 5: Filter out missing Customer_ID
feedback_df = feedback_df[feedback_df['Customer_ID'].notna()]
print("\n" + "=" * 60)
print("STEP 5: Filtered Out NA Customer_ID")
print("=" * 60)
print(feedback_df)

# Step 6: Filter out NA and blank Feedback
feedback_df = feedback_df[feedback_df['Feedback'].notna() & (feedback_df['Feedback'] != '') & (feedback_df['Feedback'] != 'Nan')]
print("\n" + "=" * 60)
print("STEP 6: Filtered Out Missing or Blank Feedback")
print("=" * 60)
print(feedback_df)

# Step 7: Filter records where Rating is not NA and Rating >= 3
feedback_df = feedback_df[feedback_df['Rating'].notna() & (feedback_df['Rating'] >= 3)]
print("\n" + "=" * 60)
print("STEP 7: Filtered Rating >= 3 (Final Cleaned Dataset)")
print("=" * 60)
print(feedback_df)

print("\nResult: Thus, the programs were written and executed to explore various variable and column filters in messy customer feedback data.")
