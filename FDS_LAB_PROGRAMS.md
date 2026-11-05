# Foundations of Data Science (FDS) Lab Programs — Complete Documentation

> **Comprehensive Lab Record Reference & Code Repository**  
> Covers Experiments 1 through 9 from the primary **FDS Lab Manual** and Experiment 10 from the **Content Beyond Syllabus** manual. Preserves original Python and R implementations, dataset specifications, output descriptions, and verified results.

---

## Table of Contents

- [Overview & Environment Setup](#overview--environment-setup)
- [Dataset & Execution Guide](#dataset--execution-guide)
- [EXPERIMENT 1: Install Data Analysis & Visualization Tool: Python (NumPy, SciPy, Pandas)](#experiment-1)
  - [Experiment 1A: NumPy Package Installation & Array Operations](#experiment-1a)
  - [Experiment 1B: SciPy Package Installation & Mathematical Functions](#experiment-1b)
  - [Experiment 1C: Pandas Package Installation & DataFrame Exploration](#experiment-1c)
- [EXPERIMENT 2: Perform Exploratory Data Analysis (EDA) on Email Dataset](#experiment-2)
- [EXPERIMENT 3: Statistical Analysis and Weather Data Manipulation using NumPy](#experiment-3)
- [EXPERIMENT 4: Data Cleaning on Messy Customer Feedback Data using R](#experiment-4)
- [EXPERIMENT 5: Analysis and Visualizations on Student Test Performance using ggplot (R)](#experiment-5)
- [EXPERIMENT 6: Retail Store Weekly Sales Exploration and Analysis using Pandas](#experiment-6)
- [EXPERIMENT 7: Spatial Data Analysis & COVID-19 Vaccination Visualization for Indian States](#experiment-7)
- [EXPERIMENT 8: Exploratory Data Analysis on Wine Quality Dataset](#experiment-8)
- [EXPERIMENT 9: Case Study — Univariate Analysis on Pima Indians Diabetes Dataset](#experiment-9)
- [EXPERIMENT 10: Visualizing Geographic Data with Basemap (Content Beyond Syllabus)](#experiment-10)
  - [10.1: Simple Mercator Coastline Map](#101-simple-mercator-coastline-map)
  - [10.2: Colored Continents & Graticules on Mercator Projection](#102-colored-continents--graticules-on-mercator-projection)
  - [10.3: Mollweide Projection with Custom Styling](#103-mollweide-projection-with-custom-styling)
  - [10.4: North American Map with State Boundaries and Rivers (Albers Equal Area)](#104-north-american-map-with-state-boundaries-and-rivers-albers-equal-area)
  - [10.5: Topographic Relief Map Zoomed to North America with Seattle Location (Lambert Conformal)](#105-topographic-relief-map-zoomed-to-north-america-with-seattle-location-lambert-conformal)
  - [10.6: Map Projections Comparison (Cylindrical, Orthographic, Conic)](#106-map-projections-comparison-cylindrical-orthographic-conic)
- [Extraction & Verification Checklist](#extraction--verification-checklist)

---

## Overview & Environment Setup

This repository contains all experimental programs prescribed in the **Foundations of Data Science (FDS)** curriculum. The laboratory experiments utilize two primary data science languages:
- **Python 3.x**: Used in Experiments 1, 2, 3, 6, 7, 8, 9, and 10.
- **R (>= 4.0)**: Used in Experiments 4 and 5.

### Python Environment Setup

To run the Python-based experiments, install the required packages:

```bash
pip install numpy scipy pandas matplotlib seaborn
```

For **Experiment 10 (Basemap)**:
```bash
pip install pillow basemap basemap-data
```
*(Or if using Anaconda: `conda install -c conda-forge basemap`)*

### R Environment Setup

For Experiments 4 and 5, launch an R console or RStudio and install the necessary CRAN libraries:

```r
install.packages(c("dplyr", "stringr", "ggplot2"))
```

---

## Dataset & Execution Guide

Several experiments rely on external tabular datasets (`.csv`). Below is the dataset directory mapping:

| Experiment | Required Dataset | Primary Columns / Variables | Expected Format |
|---|---|---|---|
| **Experiment 2** | `emails.csv` | `text`, `spam` | CSV (comma-separated) |
| **Experiment 3** | `weather_2012.csv` | `Date/Time`, `Temp (C)`, `Dew Point Temp (C)`, `Rel Hum (%)`, `Wind Spd (km/h)`, `Visibility (km)`, `Stn Press (kPa)`, `Weather` | CSV (comma-separated, datetime parsed) |
| **Experiment 4** | In-code synthetic data (`data.frame`) | `CustomerID`, `Feedback`, `Rating`, `Gender` | In-memory R dataframe |
| **Experiment 5** | In-code synthetic data (`data.frame`) | `Gender`, `Math_Score`, `Reading_Score`, `Writing_Score`, `Prep_Course` | Generated via `rnorm` and `sample` in R |
| **Experiment 6** | In-code synthetic data (`DataFrame`) | `Week`, `Store_ID`, `Weekly_Sales`, `Promotion`, `Holiday_Week` | Generated via `pd.date_range` and `np.random` |
| **Experiment 7** | In-code synthetic spatial data | `state`, `first_dose`, `fully_vaccinated`, `booster_rate`, `region` | Generated for 28 Indian States & 6 Regions |
| **Experiment 8** | `winequality-red.csv`<br>`winequality-white.csv` | `fixed acidity`, `volatile acidity`, `citric acid`, `residual sugar`, `chlorides`, `free sulfur dioxide`, `total sulfur dioxide`, `density`, `pH`, `sulphates`, `alcohol`, `quality` | CSV (**semicolon-delimited** `;`) |
| **Experiment 9** | `Pima2.csv` | `Unnamed: 0`, `npreg`, `glu`, `bp`, `skin`, `bmi`, `ped`, `age`, `type` | CSV (comma-separated, 300 rows) |

### How Students Should Update File Paths

The original source codes contain hardcoded absolute Windows paths from the laboratory workstations (e.g., `C:/Users/smily/Downloads/...` or `C:/Users/HP/OneDrive/...`). 

To run these on your local system:
1. Place the required CSV file in the same directory as your Python script or notebook.
2. Update the filename path inside `pd.read_csv()`:
   - **Relative path (recommended)**:
     ```python
     df = pd.read_csv('emails.csv')
     ```
   - **Custom absolute path (Linux / macOS)**:
     ```python
     df = pd.read_csv('/home/username/datasets/emails.csv')
     ```
   - **Custom absolute path (Windows)**:
     ```python
     df = pd.read_csv(r'C:\Users\YourUsername\Downloads\emails.csv')
     # or using forward slashes:
     df = pd.read_csv('C:/Users/YourUsername/Downloads/emails.csv')
     ```

---

## EXPERIMENT 1

### Experiment Title
**INSTALL THE DATA ANALYSIS AND VISUALIZATION TOOL: PYTHON** (NumPy, SciPy, Pandas)  
*Ex.No. 1*

---

### Experiment 1A

#### Aim
To download, install and explore the features of NumPy package.

#### Problem Description
Python is an open-source object-oriented language. It has many features of which one is the wide range of external packages. There are a lot of packages for installation and use for expanding functionalities. These packages are a repository of functions in python script. NumPy is one such package to ease array computations. To install all these python packages we use the pip- package installer. Pip is automatically installed along with Python. We can then use pip in the command line to install packages from PyPI.

**NumPy**: NumPy (Numerical Python) is an open-source library for the Python programming language. It is used for scientific computing and working with arrays. Apart from its multidimensional array object, it also provides high-level functioning tools for working with arrays.

#### Prerequisites
- Access to a terminal window / command line
- A user account with sudo privileges
- Python installed on your system

#### Program 1: Package Installation
```bash
pip install numpy
```

#### Program 2: Sample Python Program Using NumPy
```python
import numpy as np 
# Creating array object 
arr = np.array( [[ 1, 2, 3], 
[ 4, 2, 5]] ) 
# Printing type of arr object 
print("Array is of type: ", type(arr)) 
# Printing array dimensions (axes) 
print("No. of dimensions: ", arr.ndim) 
# Printing shape of array 
print("Shape of array: ", arr.shape) 
# Printing size (total number of elements) of array 
print("Size of array: ", arr.size) 
# Printing type of elements in array 
print("Array stores elements of type: ", arr.dtype) 
```

#### Output
```text
Array is of type:  <class 'numpy.ndarray'>
No. of dimensions:  2
Shape of array:  (2, 3)
Size of array:  6
Array stores elements of type:  int32
```
*(Note: Output data type may show `int64` on 64-bit Linux/macOS environments).*

#### Result
Thus, the NumPy package is downloaded, installed and the features are explored.

---

### Experiment 1B

#### Aim
To download, install and explore the features of Scipy package.

#### Problem Description
Scipy is a python library that is useful in solving many mathematical equations and algorithms. It is designed on the top of Numpy library that gives more extension of finding scientific mathematical formulae like Matrix Rank, Inverse, polynomial equations, LU Decomposition, etc. Using its high-level functions will significantly reduce the complexity of the code and helps in better analyzing the data.

#### Program 1: Package Installation
```bash
pip install scipy
```

#### Program 2: Sample Python Code Using SciPy
```python
from scipy import special 

a = special.exp10(3) 
print(a) 
b = special.exp2(3) 
print(b) 
c = special.sindg(90) 
print(c) 
 
d = special.cosdg(45) 
print(d) 
```

#### Output
```text
1000.0
8.0
1.0
0.7071067811865476
```

#### Result
Thus, the SciPy package is downloaded, installed and the features are explored.

---

### Experiment 1C

#### Aim
To download, install and explore the features of Panda packages.

#### Problem Description
Pandas is one of the most popular open-source frameworks available for Python. It is among the fastest and most easy-to-use libraries for data analysis and manipulation. Pandas dataframes are some of the most useful data structures available in any library. It has uses in every data-intensive field, including but not limited to scientific computing, data science, and machine learning.

#### Program 1: Package Installation
```bash
pip install pandas
```

#### Program 2: Sample Python Program Using Pandas (DataFrame & Series)
```python
import pandas as pd 

# Sample program - to be typed in Jupyter notebook 
data = pd.DataFrame({"x1":["y", "x", "y", "x", "x", "y"], 
"x2":range(16, 22), 
"x3":range(1, 7), 
"x4":["a", "b", "c", "d", "e", "f"], 
"x5":range(30, 24, - 1)}) 
print(data) 

s1 = pd.Series([1, 3, 4, 5, 6, 2, 9]) 
s2 = pd.Series([1.1, 3.5, 4.7, 5.8, 2.9, 9.3]) 
s3 = pd.Series(['a', 'b', 'c', 'd', 'e']) 
Data ={'first':s1, 'second':s2, 'third':s3} 

dfseries = pd.DataFrame(Data) 
print(dfseries) 
```

#### Output
```text
  x1  x2  x3 x4  x5
0  y  16   1  a  30
1  x  17   2  b  29
2  y  18   3  c  28
3  x  19   4  d  27
4  x  20   5  e  26
5  y  21   6  f  25

   first  second third
0      1     1.1     a
1      3     3.5     b
2      4     4.7     c
3      5     5.8     d
4      6     2.9     e
5      2     9.3   NaN
6      9     NaN   NaN
```

#### Result
Thus, the Panda package is downloaded, installed and the features were explored.

[Back to Top](#table-of-contents)

---

## EXPERIMENT 2

### Experiment Title
**PERFORM EXPLORATORY DATA ANALYSIS (EDA) ON WITH DATASETS LIKE EMAIL DATA SET**  
*Ex.No. 2*

### Aim
To Perform EDA on dataset using packages and get insights from data.

### Procedure
1. Import the dataset 
2. View the head of the data 
3. View the basic information of data and description of data 
4. Find the unique value of data and verify the duplication of data 
5. Plot a graph for unique value of dataset 
6. Verify the presence of null value and replace then null value 
7. Visualize the needed data 

### Dataset Required
- File: `emails.csv`
- Target path in lab code: `C:/Users/smily/Downloads/emails.csv`
- Key columns: `text`, `spam`

### Program 1: Complete EDA Python Script
```python
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

# Load the dataset 
file_path = 'C:/Users/smily/Downloads/emails.csv'  
# Adjust the path to your dataset file 
df = pd.read_csv(file_path) 
 
# Display the first few rows of the dataframe 
print(df.head()) 
# Get basic info about the dataset 
print(df.info()) 
 
# Get descriptive statistics for numeric columns 
print(df.describe()) 
 
# Check for missing values 
print(df.isnull().sum()) 

df['email_length'] = df['text'].apply(len) 
print(df) 
 
# Plot the distribution of email lengths 
plt.figure(figsize=(10, 6)) 
sns.histplot(df['email_length'], bins=50, kde=True) 
plt.title('Distribution of Email Lengths') 
plt.xlabel('Email Length') 
plt.ylabel('Frequency') 
plt.show() 

# Count emails by category 
category_counts = df['spam'].value_counts() 
# Plot email categories 
plt.figure(figsize=(10, 6)) 
category_counts.plot(kind='bar') 
plt.title('Email Categories') 
plt.xlabel('Category') 
plt.ylabel('Number of Emails') 
plt.xticks(rotation=45) 
plt.tight_layout() 
plt.show() 
```

### Output
- **Console Outputs**:
  - `df.head()` prints the first 5 records with Subject lines and spam tags.
  - `df.info()` shows total 5728 non-null rows across `text` (object) and `spam` (int64).
  - `df.describe()` outputs mean (~0.2388) and quartiles of spam distribution.
  - `df.isnull().sum()` confirms 0 missing values.
  - `print(df)` outputs the dataframe with the computed `email_length` column.
- **Visual Plots**:
  1. **Distribution of Email Lengths**: A histogram with KDE curve depicting positively skewed email character lengths concentrated heavily under 5,000 characters.
  2. **Email Categories Bar Chart**: A bar graph depicting 4,360 legitimate emails (Category 0) vs 1,368 spam emails (Category 1).

### Correction & Execution Notes
- **File Path**: Replace `'C:/Users/smily/Downloads/emails.csv'` with `'emails.csv'` if the dataset resides in your working directory.

### Result
Thus, the program to perform exploratory data analysis (EDA) on with datasets like email data set was executed.

[Back to Top](#table-of-contents)

---

## EXPERIMENT 3

### Experiment Title
**USE NUMPY ARRAYS TO COMPUTE STATISTICS AND MANIPULATE NUMERICAL WEATHER DATA**  
*Ex.No. 3*

### Aim
To write a program to work with Numpy for performing statistical analysis on weather data.

### Problem Description
Arrays in NumPy: NumPy’s main object is the homogeneous multidimensional array. 
- It is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers. 
- In NumPy dimensions are called axes. The number of axes is rank. 
- NumPy’s array class is called ndarray. It is also known by the alias array. 

Array creation & manipulation:
- Create arrays from Python lists or placeholder generators: `np.zeros`, `np.ones`, `np.full`, `np.empty`.
- Sequences generated with `arange` and `linspace`.
- Shape changes using `.reshape()` and `.flatten()`.

### Dataset Required
- File: `weather_2012.csv`
- Target path in lab code: `C:/Users/smily/Downloads/weather_2012.csv`
- Key columns: `Date/Time`, `Temp (C)`, `Dew Point Temp (C)`, `Rel Hum (%)`, `Wind Spd (km/h)`, `Visibility (km)`, `Weather`

### Program 1: Statistical Analysis Python Script
```python
import numpy as np 
import pandas as pd 

# Replace with your actual file path 
df = pd.read_csv('C:/Users/smily/Downloads/weather_2012.csv', parse_dates=['Date/Time']) 
print(df.head()) 

temps = df['Temp (C)'].to_numpy() 
winds = df['Wind Spd (km/h)'].to_numpy() 
vis = df['Visibility (km)'].to_numpy() 

print("Temp → mean:", np.nanmean(temps), "min:", np.nanmin(temps), "max:", np.nanmax(temps), "std:", np.nanstd(temps)) 
print("Wind Speed → mean:", np.nanmean(winds), "max:", np.nanmax(winds)) 

num_cloudy = np.sum(df['Weather'] == 'Cloudy') 
print("Cloudy hours:", num_cloudy) 

mask = (winds > 35) & (vis == 25) 
print("Extreme windy & clear-vis hours:", np.sum(mask)) 

df['Month'] = df['Date/Time'].dt.month 
pivot = df.pivot_table(index='Month', values='Temp (C)', aggfunc=['mean','min','max','count']) 
print(pivot) 

grouped = df.groupby('Weather')['Temp (C)'].agg(['mean','std','count']) 
print(grouped.sort_values('count', ascending=False).head()) 
```

### Output
```text
Date/Time Temp (C) Dew Point Temp (C) Rel Hum (%) Wind Spd (km/h) Visibility (km) Weather
0 2012-01-01 00:00:00 -1.8 -3.7 87 4 8.0 Fog
1 2012-01-01 01:00:00 -1.8 -3.7 87 4 8.0 Fog
...

Temp → mean: 8.798144277718308 min: -23.3 max: 33.0 std: 11.68716752009892
Wind Speed → mean: 14.945469034608382 max: 83.0
Cloudy hours: 1728
Extreme windy & clear-vis hours: 58

Monthly Pivot Table:
       mean    min    max  count
Month                           
1     -7.37  -23.3   14.5    744
2     -4.23  -16.9    6.1    696
...

Top Weather Conditions Grouped:
               mean        std  count
Weather                              
Mainly Clear  12.59      12.49   2106
Mostly Cloudy 10.57      11.31   2069
Cloudy         7.97      11.40   1728
Clear         13.63      12.13   1326
Snow          -4.88       4.15    390
```

### Correction & Execution Notes
- **Indentation Correction**: In the manual on page 12, `print(grouped.sort_values('count', ascending=False).head())` has three leading spaces. In standard Python script execution, remove the 3 leading spaces to prevent an `IndentationError`.

### Result
Thus, the program to perform statistical analysis on weather data using Numpy arrays were executed.

[Back to Top](#table-of-contents)

---

## EXPERIMENT 4

### Experiment Title
**DATA CLEANING ON MESSY CUSTOMER FEEDBACK DATA USING R**  
*Ex.No. 4*

### Aim
To explore various variable and column filters in R for cleaning messy customer feedback data.

### Procedure
1. Import `dplyr` and `stringr` library 
2. Create a dataset 
3. Using filter functions rearrange and normalize the data 
4. Using filter functions remove NA and apply conditions on data 

### Language
**R**

### Program 1: Complete R Data Cleaning Script
```r
library(dplyr) 
library(stringr) 

# Step 1: Create initial messy dataframe 
feedback_df <- data.frame( 
  CustomerID = c(101, 102, 103, NA, 105, 106), 
  Feedback = c("Good service", "bad Service!!", NA, "  excellent!! ", "Average ", ""), 
  Rating = c(5, 1, NA, 5, 3, 2), 
  Gender = c("Male", "Female", "F", "female", "MALE", "M"), 
  stringsAsFactors = FALSE 
) 
print(feedback_df) 

# Step 2: Rename CustomerID to Customer_ID
feedback_df <- feedback_df %>%  
  rename(Customer_ID = CustomerID) 

# Step 3: Clean whitespace, case, and remove punctuation
feedback_df <- feedback_df %>% 
  mutate( 
    Feedback = str_trim(Feedback),                     # Remove extra spaces 
    Feedback = str_to_sentence(Feedback),              # Capitalize first letter 
    Feedback = str_replace_all(Feedback, "[^[:alnum:] ]", "")  # Remove punctuation 
  ) 

# Step 4: Normalize Gender categories
feedback_df <- feedback_df %>% 
  mutate( 
    Gender = str_to_lower(Gender), 
    Gender = case_when( 
      Gender %in% c("male", "m") ~ "Male", 
      Gender %in% c("female", "f") ~ "Female", 
      TRUE ~ "Other" 
    ) 
  ) 
print(feedback_df) 

# Step 5: Filter out NA Customer_ID
feedback_df <- feedback_df %>% 
  filter(!is.na(Customer_ID)) 
print(feedback_df) 

# Step 6: Filter out missing or blank Feedback
feedback_df <- feedback_df %>% 
  filter(!is.na(Feedback) & Feedback != "") 
print(feedback_df) 

# Step 7: Filter records where Rating >= 3
feedback_df <- feedback_df %>% 
  filter(!is.na(Rating) & Rating >= 3) 
print(feedback_df) 
```

### Output
- **Raw Input**:
  ```text
    CustomerID       Feedback Rating Gender
  1        101   Good service      5   Male
  2        102  bad Service!!      1 Female
  3        103           <NA>     NA      F
  4         NA    excellent!!      5 female
  5        105       Average       3   MALE
  6        106                     2      M
  ```
- **After Text Cleaning & Gender Standardization**:
  ```text
    Customer_ID     Feedback Rating Gender
  1         101 Good service      5   Male
  2         102  Bad service      1 Female
  3         103         <NA>     NA Female
  4          NA    Excellent      5 Female
  5         105      Average      3   Male
  6         106                   2   Male
  ```
- **After Filter (!is.na(Customer_ID))**:
  ```text
    Customer_ID     Feedback Rating Gender
  1         101 Good service      5   Male
  2         102  Bad service      1 Female
  3         103         <NA>     NA Female
  4         105      Average      3   Male
  5         106                   2   Male
  ```
- **After Filter (!is.na(Feedback) & Feedback != "")**:
  ```text
    Customer_ID     Feedback Rating Gender
  1         101 Good service      5   Male
  2         102  Bad service      1 Female
  3         105      Average      3   Male
  ```
- **After Filter (Rating >= 3)**:
  ```text
    Customer_ID     Feedback Rating Gender
  1         101 Good service      5   Male
  2         105      Average      3   Male
  ```

### Result
Thus, the R programs were written and executed to explore various variable and column filters in messy customer feedback data.

[Back to Top](#table-of-contents)

---

## EXPERIMENT 5

### Experiment Title
**PERFORM ANALYSIS AND VISUALIZATIONS ON STUDENT TEST PERFORMANCE DATA USING GGPLOT**  
*Ex.No. 5*

### Aim
To perform various analysis and visualization on student test performance using ggplot features.

### Procedure
1. Import `dplyr` and `ggplot` library 
2. Create the dataframe  
3. Perform analysis using features of ggplot 
4. Visualize the data using histogram, boxplot, violin plot and scatter plot  

### Language
**R**

### Program 1: Complete R ggplot Visualization Script
```r
# Step 1: Create student performance dataframe
student_data <- data.frame( 
  Gender = sample(c("Male", "Female"), 100, replace = TRUE), 
  Math_Score = rnorm(100, mean = 65, sd = 15), 
  Reading_Score = rnorm(100, mean = 70, sd = 10), 
  Writing_Score = rnorm(100, mean = 68, sd = 12), 
  Prep_Course = sample(c("Completed", "None"), 100, replace = TRUE) 
) 
print(head(student_data)) 

library(ggplot2) 

# Step 2: Distribution of Math Scores (Histogram)
ggplot(student_data, aes(x = Math_Score)) + 
  geom_histogram(binwidth = 5, fill = "steelblue", color = "black") + 
  theme_minimal() + 
  labs(title = "Distribution of Math Scores", x = "Math Score", y = "Count") 

# Step 3: Math Scores by Gender (Boxplot)
ggplot(student_data, aes(x = Gender, y = Math_Score, fill = Gender)) + 
  geom_boxplot() + 
  theme_minimal() + 
  labs(title = "Math Scores by Gender", x = "Gender", y = "Math Score") 

# Step 4: Reading Scores by Test Prep Course (Violin Plot)
ggplot(student_data, aes(x = Prep_Course, y = Reading_Score, fill = Prep_Course)) + 
  geom_violin(trim = FALSE) + 
  theme_minimal() + 
  labs(title = "Reading Scores by Test Prep Course", x = "Test Preparation Course", y = "Reading Score") 

# Step 5: Math vs Reading Scores by Gender (Scatter Plot)
ggplot(student_data, aes(x = Math_Score, y = Reading_Score, color = Gender)) + 
  geom_point(alpha = 0.7) + 
  theme_minimal() + 
  labs(title = "Math vs Reading Scores", x = "Math Score", y = "Reading Score") 

# Step 6: Compute Average Score and plot across Test Prep Course (Boxplot)
student_data$Average_Score <- rowMeans(student_data[, c("Math_Score", "Reading_Score", "Writing_Score")]) 

ggplot(student_data, aes(x = Prep_Course, y = Average_Score, fill = Prep_Course)) + 
  geom_boxplot() + 
  theme_minimal() + 
  labs(title = "Average Scores by Test Preparation Course", x = "Test Preparation", y = "Average Score") 
```

### Output
- `head(student_data)` outputs first 6 student records with generated scores and test prep status.
- **Plot 1 (Histogram)**: Steel-blue histogram with black borders displaying bell-curve distribution of math scores centered at 65.
- **Plot 2 (Boxplot)**: Gender comparison boxplot highlighting median, 25th/75th percentiles, and potential outliers.
- **Plot 3 (Violin Plot)**: Symmetrical kernel density violin plot comparing spread of reading scores for students who Completed vs None.
- **Plot 4 (Scatter Plot)**: Two-variable point plot with alpha transparency showing correlation between math and reading proficiencies colored by Gender.
- **Plot 5 (Boxplot)**: Boxplot comparing composite average score distributions across test preparation courses.

### Result
Thus, the R programs were written and executed to perform analysis and visualization on student test performance data using ggplot features.

[Back to Top](#table-of-contents)

---

## EXPERIMENT 6

### Experiment Title
**USE PANDAS TO EXPLORE AND ANALYZE A MOCK DATASET OF A RETAIL STORE’S WEEKLY SALES**  
*Ex.No. 6*

### Aim
To explore, analyze and visualize a mock retail store’s weekly sales dataset using features of pandas.

### Language
**Python**

### Program 1: Retail Sales Analysis Script
```python
import pandas as pd 
import numpy as np 
 
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
print(data) 

print("First few rows:") 
print(df.head()) 
 
print("
Summary statistics:") 
print(df.describe()) 
 
print("
Data types:") 
print(df.dtypes) 
 
print("
Missing values:") 
print(df.isnull().sum()) 

import matplotlib.pyplot as plt 
 
# Plot 1: Total weekly sales trend
df.groupby("Week")["Weekly_Sales"].sum().plot(marker='o', figsize=(10, 5)) 
plt.title("Total Weekly Sales Over Time") 
plt.xlabel("Week") 
plt.ylabel("Sales ($)") 
plt.grid(True) 
plt.show() 

# Plot 2: Average weekly sales by store
df.groupby("Store_ID")["Weekly_Sales"].mean().plot(kind='bar', color='skyblue') 
plt.title("Average Weekly Sales by Store") 
plt.ylabel("Average Sales") 
plt.show() 

# Plot 3: Impact of promotion on sales
df.groupby("Promotion")["Weekly_Sales"].mean().plot(kind='bar', color=['red', 'green']) 
plt.xticks([0, 1], ['No Promotion', 'Promotion Active'], rotation=0) 
plt.title("Average Sales: Promotion vs No Promotion") 
plt.ylabel("Average Weekly Sales") 
plt.show() 

# Correlation matrix
print("
Correlation Matrix:") 
print(df.corr(numeric_only=True)) 
 
# Optional heatmap using seaborn 
import seaborn as sns 
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm') 
plt.title("Correlation Heatmap") 
plt.show() 
```

### Output
- `df.head()` displays first 5 mock weekly entries (e.g. 2023-01-01, Store 103, $24,423).
- `df.describe()` outputs summary statistics including mean, standard deviation, and quartiles.
- `df.dtypes` lists timestamps and 64-bit integer formats.
- `df.isnull().sum()` confirms 0 missing values.
- **Plot 1**: Time-series curve tracking weekly store revenue trends across January - March 2023.
- **Plot 2**: Bar chart comparing sales volume performance between Store 101, Store 102, and Store 103.
- **Plot 3**: Bar graph contrasting average weekly sales under non-promotional vs promotional conditions.
- **Plot 4**: Seaborn correlation matrix heatmap displaying pairwise Pearson correlation coefficients.

### Result
Thus, the python code was written and executed to explore, analyze and visualize a mock retail store’s weekly sales dataset using features of pandas.

[Back to Top](#table-of-contents)

---

## EXPERIMENT 7

### Experiment Title
**USE SPATIAL DATASETS TO MAP VACCINATION RATES BY STATE WITH INTERACTIVE EFFECTS LIKE MOUSE ROLLOVER, TOOLTIPS, AND USER-SELECTED METRICS**  
*Ex.No. 7*

### Aim
To generate and visualize sample COVID-19 vaccination data for Indian states by creating bar charts, scatter plots, and heatmaps, in order to compare first dose, fully vaccinated, and booster dose rates across different regions.

### Procedure
1. Import libraries – pandas, seaborn, matplotlib, numpy. 
2. Define states & regions – list of Indian states with their regional groupings. 
3. Generate sample vaccination data – random values for first dose, fully vaccinated, and booster rates. 
4. Create Data Frame – combine states, vaccination data, and regions. 
5. Sort states – order by first dose rate (descending). 
6. Plot 1 (Bar chart) – compare first dose vs fully vaccinated for top states. 
7. Plot 2 (Scatter plot) – show relation between first dose and booster rates, colored by region. 
8. Plot 3 (Heatmap) – display vaccination metrics for top states. 

### Language
**Python**

### Program 1: Indian States Vaccination Visualization Script
```python
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np 
 
# Style 
sns.set_style("whitegrid") 
plt.rcParams['figure.figsize'] = (12, 8) 
 
# Indian states 
states = [ 
    'Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh', 
    'Goa','Gujarat','Haryana','Himachal Pradesh','Jharkhand', 
    'Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur', 
    'Meghalaya','Mizoram','Nagaland','Odisha','Punjab', 
    'Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura', 
    'Uttar Pradesh','Uttarakhand','West Bengal' 
] 
 
# Regions 
regions = [ 
    'South','Northeast','Northeast','North','Central', 
    'West','West','North','North','East', 
    'South','South','Central','West','Northeast', 
    'Northeast','Northeast','Northeast','East','North', 
    'West','Northeast','South','South','Northeast', 
    'North','North','East' 
] 

# Random vaccination data 
np.random.seed(42) 
df = pd.DataFrame({ 
    'state': states, 
    'first_dose': np.random.uniform(40, 80, len(states)), 
}) 
df['fully_vaccinated'] = df['first_dose'] * np.random.uniform(0.8, 0.95, len(df)) 
df['booster_rate'] = df['fully_vaccinated'] * np.random.uniform(0.5, 0.8, len(df)) 
df['region'] = regions 
df = df.sort_values('first_dose', ascending=False) 
 
# --- Plot 1: Bar comparison --- 
top_states = df.head(15).melt(id_vars=['state'],  
                              value_vars=['first_dose','fully_vaccinated'], 
                              var_name='type', value_name='rate') 
 
sns.barplot(data=top_states, x='state', y='rate', hue='type', palette='Set2') 
plt.title('First Dose vs Fully Vaccinated (Top 15 States)') 
plt.xticks(rotation=60) 
plt.tight_layout() 
plt.show() 
 
# --- Plot 2: Scatter --- 
sns.scatterplot(data=df, x='first_dose', y='booster_rate',  
                hue='region', s=100, palette='deep') 
 
for x,y,label in zip(df['first_dose'], df['booster_rate'], df['state']): 
    plt.text(x+0.3, y+0.3, label, fontsize=8) 
 
plt.title('First Dose vs Booster Rate') 
plt.grid(True, alpha=0.3) 
plt.tight_layout() 
plt.show() 
 
# --- Plot 3: Heatmap --- 
top_10 = df.head(10).set_index('state')[['first_dose','fully_vaccinated','booster_rate']] 
sns.heatmap(top_10, annot=True, fmt='.1f', cmap='YlOrRd', linewidths=0.5, 
            cbar_kws={'label': 'Vaccination Rate (%)'}) 
plt.title('Vaccination Rates Heatmap - Top 10 States') 
plt.tight_layout() 
plt.show() 
```

### Output
- **Plot 1**: Grouped bar chart with `Set2` color palette comparing dose 1 uptake vs completion percentage across states like Kerala, Arunachal Pradesh, Haryana, and Madhya Pradesh.
- **Plot 2**: Scatter plot displaying positive correlation between first dose and booster coverage, with dots colored by Region (South, Northeast, North, Central, East, West) and annotated with state labels.
- **Plot 3**: Heatmap displaying vaccination rate percentages across first dose, fully vaccinated, and booster doses for the top 10 states.

### Result
Thus, the python code was written and executed to explore, how data visualization can be used to compare vaccination progress across different states and regions in India.

[Back to Top](#table-of-contents)

---

## EXPERIMENT 8

### Experiment Title
**PERFORM EDA ON WINE QUALITY DATA SET**  
*Ex.No. 8*

### Aim
To write a python program for EDA on Wine Quality Data Set.

### Procedure
1. Import library  
2. Import wine dataset  
3. Perform EDA to display information, description of data.  
4. Analyse the content of alcohol consumption and visualize it 

### Datasets Required
- Files: `winequality-red.csv` and `winequality-white.csv`
- Target paths in lab code: 
  - `C:/Users/smily/Downloads/winequality-red.csv`
  - `C:/Users\smily/Downloads/winequality-white.csv`
- Delimiter: Semicolon (`;`)

### Program 1: Wine Quality EDA Python Script
```python
import pandas as pd 

# Load red and white wine quality datasets
df_red = pd.read_csv("C:/Users/smily/Downloads/winequality-red.csv", delimiter=";") 
df_white = pd.read_csv("C:/Users\smily/Downloads/winequality-white.csv", delimiter=";") 

df_red.head() 
#df_red.columns Index(['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar','chlorides', 'free sulfur dioxide', 'total sulfur dioxide','density','pH','sulphates','alcohol', 'quality'],dtype='object')  
df_red.iloc[100:110] 

df_red.dtypes 
df_red.describe() 
df_red.info() 

import seaborn as sns  
sns.set(rc={'figure.figsize': (14, 8)})  
sns.countplot(df_red, x="quality") 

sns.distplot(df_red['alcohol']) 

from scipy.stats import skew 
skew(df_red['alcohol']) 
```

### Output
- `df_red.head()` and `df_red.iloc[100:110]` displaying rows 100 to 109.
- `df_red.dtypes` showing float64 for physicochemical attributes and int64 for quality.
- `df_red.describe()` with count (1599), mean, std, min, quartiles, max.
- `df_red.info()` showing DataFrame info (1599 non-null entries, 12 columns).
- Countplot of `quality` (distribution peaks at 5 and 6).
- Distplot of `alcohol` content (showing right-skewed distribution).
- Skewness value: `0.8600210646566755` (positive skewness).

### Correction & Execution Notes
- **Local File Paths**: Update `"C:/Users/smily/Downloads/winequality-red.csv"` to `"winequality-red.csv"` (or your local path).
- **Seaborn Modern Syntax**:
  - In newer versions of Seaborn (>= 0.12), `sns.countplot(data=df_red, x="quality")` is standard syntax.
  - `sns.distplot()` has been superseded by `sns.histplot(df_red['alcohol'], kde=True)`.

### Result
Thus, the program to execute the EDA on wine dataset was executed successfully.

[Back to Top](#table-of-contents)

---

## EXPERIMENT 9

### Experiment Title
**CASE STUDY - USE THE DIABETES DATA SET FROM PIMA INDIAN’S DIABETES**  
*Ex.No. 9*

### Aim
To perform Univariate analysis like Frequency, Mean, Median, Mode, Variance, Standard Deviation, Skewness and Kurtosis in pima Indians dataset.

### Dataset Required
- File: `Pima2.csv`
- Target path in lab code: `C:/Users/HP/OneDrive/Desktop/RESEARCH/Data/Pima2.csv`
- Dimensions: 300 rows x 9 columns
- Attributes: `Unnamed: 0`, `npreg`, `glu`, `bp`, `skin`, `bmi`, `ped`, `age`, `type`

### Program 1: Univariate Statistical Analysis Python Script
```python
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd  
from scipy.stats import skew 
from scipy.stats import kurtosis 
import statistics 
 
df = pd.read_csv('C:/Users/HP/OneDrive/Desktop/RESEARCH/Data/Pima2.csv') 
print('THE SHAPE OF THE DATASET IS 
',df.shape) 
print('THE DATA TYPES ARE :
',df.dtypes) 
print('THE DESCRIPTION OF THE DATASET IS:
',df.describe().T) 
df.plot(kind='density', subplots=True, layout=(3,3), sharex=False) 
 
print('THE FREQUENCY OF PREGNANCIES IS:
',df['npreg'].value_counts()) 
preg = np.array(df['npreg']) 
print('MEAN                       :',statistics.mean(preg)) 
print('MEDIAN                     :',statistics.median(preg)) 
print('MODE                       :',statistics.multimode(preg)) 
print('VARIANCE                   :',statistics.variance(preg)) 
print('sTANDARS DEVIATION         :',statistics.stdev(preg)) 
if (skew(preg)>0) : 
    print("POSITIVE  SKEWNESS 
") 
elif (skew(preg)<0) : 
    print("NEGATIVE  SKEWNESS 
") 
else  : 
    print("NO  SKEWNESS 
") 
print('KURTOSIS',kurtosis(preg)) 
 
print('THE FREQUENCY OF GLOCOSE IS:
',df['glu'].value_counts()) 
G = np.array(df['glu']) 
print('MEAN                       :',statistics.mean(G)) 
print('MEDIAN                     :',statistics.median(G)) 
print('MODE                       :',statistics.multimode(G)) 
print('VARIANCE                   :',statistics.variance(G)) 
print('sTANDARS DEVIATION         :',statistics.stdev(G)) 
if (skew(G)>0) : 
    print("POSITIVE  SKEWNESS 
") 
elif (skew(G)<0) : 
    print("NEGATIVE  SKEWNESS 
") 
else  : 
    print("NO  SKEWNESS 
") 
print('KURTOSIS',kurtosis(G)) 
```

### Output
```text
THE SHAPE OF THE DATASET IS  
 (300, 9) 
THE DATA TYPES ARE : 
 Unnamed: 0      int64 
npreg           int64 
glu             int64 
bp            float64 
skin          float64 
bmi           float64 
ped           float64 
age             int64 
type           object 
dtype: object 
THE DESCRIPTION OF THE DATASET IS: 
             count        mean        std  ...      50%        75%      max 
Unnamed: 0  300.0  150.500000  86.746758  ...  150.500  225.25000  300.000 
npreg       300.0    3.786667   3.306195  ...    3.000    6.00000   14.000 
glu         300.0  123.743333  30.011549  ...  121.000  142.00000  199.000 
bp          287.0   72.320557  11.704477  ...   72.000   80.00000  114.000 
skin        202.0   29.153465  11.682415  ...   29.000   36.00000   99.000 
bmi         297.0   32.052862   6.492933  ...   32.000   36.50000   52.900 
ped         300.0    0.435657   0.294600  ...    0.336    0.58675    2.288 
age         300.0   33.096667  11.578176  ...   29.000   40.00000   72.000 
[8 rows x 8 columns] 

THE FREQUENCY OF PREGNANCIES IS: 
 1     51 
 0     44 
 2     41 
 4     35 
 3     26 
 5     22 
 6     19 
 7     17 
 8     15 
 9      9 
 10     8 
 12     6 
 13     3 
 14     2 
 11     2 
Name: npreg, dtype: int64 
MEAN                       : 3 
MEDIAN                     : 3.0 
MODE                       : [1] 
VARIANCE                   : 10 
sTANDARS DEVIATION         : 3.1622776601683795 
POSITIVE  SKEWNESS  
KURTOSIS 0.20897562301271444 

THE FREQUENCY OF GLOCOSE IS: 
 100    8 
 125    8 
 111    6 
 95     6 
 139    6 
      .. 
 152    1 
 149    1 
 135    1 
 198    1 
 56     1 
Name: glu, Length: 108, dtype: int64 
MEAN                       : 123 
MEDIAN                     : 121.0 
MODE                       : [100, 125] 
VARIANCE                   : 900 
sTANDARS DEVIATION         : 30.0 
POSITIVE  SKEWNESS  
KURTOSIS -0.19604758469298522 
```
- **Visual Density Subplots**: 3x3 multi-panel plot showing smooth estimated density distributions for all numerical columns.

### Correction & Execution Notes
- **String Preservations**: The manual original typos `'sTANDARS DEVIATION         :'` and `'THE FREQUENCY OF GLOCOSE IS:'` are preserved as in original lab code.
- **File Path**: Replace `'C:/Users/HP/OneDrive/Desktop/RESEARCH/Data/Pima2.csv'` with your local file path.

### Result
Thus, the univariate analysis like Frequency, Mean, Median, Mode, Variance, Standard Deviation, Skewness and Kurtosis in pima Indians dataset was executed successfully.

[Back to Top](#table-of-contents)

---

## EXPERIMENT 10

### Experiment Title
**CONTENT BEYOND SYLLABUS: VISUALIZING GEOGRAPHIC DATA WITH BASEMAP**  
*Ex.No. 10*

### Aim
To visualizing geographic data with basemap

### Overview & Methods
Basemap is a great tool for creating maps using python in a simple way. It’s a matplotlib extension, so it has got all its features to create data visualizations, and adds the geographical projections and some datasets to be able to plot coast lines, countries, and so on directly from the library.

**Key Basemap Methods from Manual**:
- **Physical boundaries and bodies of water**:
  - `drawcoastlines()`: Draw continental coast lines
  - `drawlsmask()`: Draw a mask between the land and sea, for use with projecting images
  - `drawmapboundary()`: Draw the map boundary, including the fill color for oceans
  - `drawrivers()`: Draw rivers on the map
  - `fillcontinents()`: Fill the continents with a given color; optionally fill lakes with another color
- **Political boundaries**:
  - `drawcountries()`: Draw country boundaries
  - `drawstates()`: Draw US state boundaries
  - `drawcounties()`: Draw county boundaries
- **Map features**:
  - `drawgreatcircle()`: Draw a great circle between two points
  - `drawparallels()`: Draw lines of constant latitude
  - `drawmeridians()`: Draw lines of constant longitude
  - `drawmapscale()`: Draw a linear scale on the map
- **Whole-globe images**:
  - `bluemarble()`: Project NASA's blue marble image onto the map
  - `shadedrelief()`: Project a shaded relief image onto the map
  - `etopo()`: Draw an etopo relief image onto the map
  - `warpimage()`: Project a user-provided image onto the map

### Installation Steps
```bash
pip install pillow
pip install basemap
```

---

### 10.1: Simple Mercator Coastline Map

#### Program 1
```python
from mpl_toolkits.basemap import Basemap  
import matplotlib.pyplot as plt  
import numpy as np  
%matplotlib inline  
import warnings  
import matplotlib.cbook  
warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)  

fig = plt.figure(num=None, figsize=(12, 8))  
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180, resolution='c')  
m.drawcoastlines()  
plt.title("Mercator Projection")  
plt.show() 
```

#### Output
Displays a clean global continental coastline outline mapped under a Mercator cylindrical projection between latitudes -80° and 80°.

---

### 10.2: Colored Continents & Graticules on Mercator Projection

#### Program 1a: Coding for Coloring
```python
fig = plt.figure(num=None, figsize=(12, 8))  
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180, resolution='c')  
m.drawcoastlines()  
m.fillcontinents(color='tan', lake_color='lightblue')  

# Draw parallels and meridians 
m.drawparallels(np.arange(-90., 91., 30.), labels=[True, True, False, False], dashes=[2, 2])  
m.drawmeridians(np.arange(-180., 181., 60.), labels=[False, False, False, True], dashes=[2, 2])  
m.drawmapboundary(fill_color='lightblue')  
plt.title("Mercator Projection") 
plt.show()
```

#### Output
A fully rendered Mercator projection map featuring:
- Continents colored in `tan`
- Lakes and oceans rendered in `lightblue`
- Dashed latitude graticules every 30° with left and right labels
- Dashed longitude graticules every 60° with bottom labels

---

### 10.3: Mollweide Projection with Custom Styling

#### Program 1b: Same Sequence of Commands with Mollweide Projection
```python
fig = plt.figure(num=None, figsize=(12, 8))  
m = Basemap(projection='moll', lon_0=0, resolution='c')  
m.drawcoastlines()  
m.fillcontinents(color='purple', lake_color='lightblue')  

# Draw parallels and meridians 
m.drawparallels(np.arange(-90., 91., 30.), labels=[True, True, False, False], dashes=[2, 2])  
m.drawmeridians(np.arange(-180., 181., 60.), labels=[False, False, False, False], dashes=[2, 2])  
m.drawmapboundary(fill_color='lightblue')  
plt.title("Mollweide Projection") 
plt.show()
```

#### Output
An elliptical pseudocylindrical Mollweide map centered at longitude 0°, displaying purple landmasses surrounded by light-blue oceans with latitude lines.

---

### 10.4: North American Map with State Boundaries and Rivers (Albers Equal Area)

#### Program 2a: North America Map
```python
fig = plt.figure(num=None, figsize=(12, 8))  
m = Basemap(width=6000000, height=4500000, resolution='c', projection='aea', 
            lat_1=35., lat_2=45, lon_0=-100, lat_0=40)  
m.drawcoastlines(linewidth=0.5)  
m.fillcontinents(color='tan', lake_color='lightblue')  

# Draw parallels and meridians 
m.drawparallels(np.arange(-90., 91., 15.), labels=[True, True, False, False], dashes=[2, 2])  
m.drawmeridians(np.arange(-180., 181., 15.), labels=[False, False, False, True], dashes=[2, 2])  
m.drawmapboundary(fill_color='lightblue')  

# Add political boundaries & rivers
m.drawcountries(linewidth=2, linestyle='solid', color='k')  
m.drawstates(linewidth=0.5, linestyle='solid', color='k')  
m.drawrivers(linewidth=0.5, linestyle='solid', color='blue') 
plt.show()
```

#### Output
Detailed regional map centered on North America with:
- Thick black lines (`linewidth=2`) for international country boundaries
- Thin black lines (`linewidth=0.5`) for state lines
- Blue lines (`linewidth=0.5`) depicting major river paths
- Curved conic projection graticules spaced every 15°

---

### 10.5: Topographic Relief Map Zoomed to North America with Seattle Location (Lambert Conformal)

#### Program 2b: Seattle Location on Topographic Map
```python
fig = plt.figure(figsize=(8, 8))  
m = Basemap(projection='lcc', resolution=None,  
            width=8E6, height=8E6,  
            lat_0=45, lon_0=-100)  
m.etopo(scale=0.5, alpha=0.5)  

# Map (long, lat) to (x, y) for plotting  
x, y = m(-122.3, 47.6)  
plt.plot(x, y, 'ok', markersize=5)  
plt.text(x, y, ' Seattle', fontsize=12) 
plt.show()
```

#### Output
A topographic relief map of the North American continent generated via `etopo()`, featuring a black point marker and a text label indicating Seattle at coordinates (-122.3° W, 47.6° N).

---

### 10.6: Map Projections Comparison (Cylindrical, Orthographic, Conic)

#### Shared Setup & Helper Routine
```python
from itertools import chain  

def draw_map(m, scale=0.2):  
    # Draw a shaded-relief image  
    m.shadedrelief(scale=scale)  
    # Lats and longs are returned as a dictionary  
    lats = m.drawparallels(np.linspace(-90, 90, 13))  
    lons = m.drawmeridians(np.linspace(-180, 180, 13))  
    # Keys contain the plt.Line2D instances  
    lat_lines = chain(*(tup[1][0] for tup in lats.items()))  
    lon_lines = chain(*(tup[1][0] for tup in lons.items()))  
    all_lines = chain(lat_lines, lon_lines)  
    # Cycle through these lines and set the desired style  
    for line in all_lines:  
        line.set(linestyle='-', alpha=0.3, color='w')  
```

#### Program 2c: Cylindrical Projection
```python
fig = plt.figure(figsize=(8, 6), edgecolor='w')  
m = Basemap(projection='cyl', resolution=None,  
            llcrnrlat=-90, urcrnrlat=90,  
            llcrnrlon=-180, urcrnrlon=180)  
draw_map(m) 
plt.show()
```

#### Program 2d: Orthographic (Perspective) Projection
```python
fig = plt.figure(figsize=(8, 8))  
m = Basemap(projection='ortho', resolution=None,  
            lat_0=50, lon_0=0)  
draw_map(m) 
plt.show()
```

#### Program 2e: Conic Projection (Lambert Conformal)
```python
fig = plt.figure(figsize=(8, 8))  
m = Basemap(projection='lcc', resolution=None,  
            lon_0=0, lat_0=50, lat_1=45, lat_2=55,  
            width=1.6E7, height=1.2E7)  
draw_map(m) 
plt.show()
```

#### Output
- **Cylindrical Projection (`cyl`)**: Equidistant rectangular projection of the full world with horizontal and vertical white coordinate grid lines over shaded relief.
- **Orthographic Projection (`ortho`)**: A realistic 3D globe visualization showing half the Earth as viewed from deep space, centered at latitude 50° N and longitude 0°.
- **Conic Projection (`lcc`)**: Conic projection showing the European and Eurasian landmasses between standard parallels 45° N and 55° N.

#### Result
Thus, visualizing geographic data with basemap was implemented and executed successfully.

[Back to Top](#table-of-contents)

---

## Extraction & Verification Checklist

| Experiment | PDF Source | Language | Complete Code Extracted | Original Aim Preserved | Output Detailed | Original Result Preserved | Verified Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Exp 1A** | FDS EXP 1-9 (p. 1-2) | Python | Yes | Yes | Yes | Yes | Verified |
| **Exp 1B** | FDS EXP 1-9 (p. 3-4) | Python | Yes | Yes | Yes | Yes | Verified |
| **Exp 1C** | FDS EXP 1-9 (p. 5-7) | Python | Yes | Yes | Yes | Yes | Verified |
| **Exp 2** | FDS EXP 1-9 (p. 8-10) | Python | Yes | Yes | Yes | Yes | Verified |
| **Exp 3** | FDS EXP 1-9 (p. 11-13) | Python | Yes | Yes | Yes | Yes | Verified |
| **Exp 4** | FDS EXP 1-9 (p. 14-15) | R | Yes | Yes | Yes | Yes | Verified |
| **Exp 5** | FDS EXP 1-9 (p. 16-19) | R | Yes | Yes | Yes | Yes | Verified |
| **Exp 6** | FDS EXP 1-9 (p. 20-23) | Python | Yes | Yes | Yes | Yes | Verified |
| **Exp 7** | FDS EXP 1-9 (p. 24-27) | Python | Yes | Yes | Yes | Yes | Verified |
| **Exp 8** | FDS EXP 1-9 (p. 28-31) | Python | Yes | Yes | Yes | Yes | Verified |
| **Exp 9** | FDS EXP 1-9 (p. 32-34) | Python | Yes | Yes | Yes | Yes | Verified |
| **Exp 10** | Content Beyond Syllabus (p. 1-11) | Python | Yes | Yes | Yes | Yes | Verified |
