"""
EXPERIMENT 5
Title: PERFORM ANALYSIS AND VISUALIZATIONS ON STUDENT TEST PERFORMANCE DATA USING PYTHON / GGPLOT
Aim: To perform various analysis and visualization on student test performance.
Note: Originally written in R using ggplot2 in the lab syllabus manual.
      This file provides the Python equivalent using Matplotlib & Seaborn.
      The original R script is also provided in: exp5_student_performance_ggplot.R
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seed for reproducibility
np.random.seed(42)

# Step 1: Create student test performance dataset
n = 100
student_data = pd.DataFrame({
    'Gender': np.random.choice(["Male", "Female"], size=n),
    'Math_Score': np.random.normal(loc=65, scale=15, size=n),
    'Reading_Score': np.random.normal(loc=70, scale=10, size=n),
    'Writing_Score': np.random.normal(loc=68, scale=12, size=n),
    'Prep_Course': np.random.choice(["Completed", "None"], size=n)
})

print("--- First 6 Rows of Student Performance Data ---")
print(student_data.head())

sns.set_theme(style="whitegrid")

# Step 2: Distribution of Math Scores (Histogram)
plt.figure(figsize=(8, 5))
sns.histplot(student_data['Math_Score'], binwidth=5, color="steelblue", edgecolor="black", kde=False)
plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Step 3: Math Scores by Gender (Boxplot)
plt.figure(figsize=(8, 5))
sns.boxplot(data=student_data, x="Gender", y="Math_Score", hue="Gender", palette="Set2", legend=False)
plt.title("Math Scores by Gender")
plt.xlabel("Gender")
plt.ylabel("Math Score")
plt.tight_layout()
plt.show()

# Step 4: Reading Scores by Test Prep Course (Violin Plot)
plt.figure(figsize=(8, 5))
sns.violinplot(data=student_data, x="Prep_Course", y="Reading_Score", hue="Prep_Course", palette="Pastel1", cut=0, legend=False)
plt.title("Reading Scores by Test Prep Course")
plt.xlabel("Test Preparation Course")
plt.ylabel("Reading Score")
plt.tight_layout()
plt.show()

# Step 5: Math vs Reading Scores by Gender (Scatter Plot)
plt.figure(figsize=(8, 5))
sns.scatterplot(data=student_data, x="Math_Score", y="Reading_Score", hue="Gender", alpha=0.7, palette="Set1", s=70)
plt.title("Math vs Reading Scores")
plt.xlabel("Math Score")
plt.ylabel("Reading Score")
plt.tight_layout()
plt.show()

# Step 6: Average score calculation & Boxplot by Test Prep Course
student_data['Average_Score'] = student_data[['Math_Score', 'Reading_Score', 'Writing_Score']].mean(axis=1)

plt.figure(figsize=(8, 5))
sns.boxplot(data=student_data, x="Prep_Course", y="Average_Score", hue="Prep_Course", palette="Set3", legend=False)
plt.title("Average Scores by Test Preparation Course")
plt.xlabel("Test Preparation")
plt.ylabel("Average Score")
plt.tight_layout()
plt.show()

print("\nResult: Thus, the programs were written and executed to perform analysis and visualization on student test performance data.")
