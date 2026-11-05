# Foundations of Data Science (FDS) Lab Programs

This repository contains standalone, runnable code files for all 10 experiments from the **Foundations of Data Science (FDS)** curriculum, including Experiments 1–9 from the main lab manual and Experiment 10 from the Content Beyond Syllabus manual.

## Program Files Overview

| Experiment | File Name | Language | Description | Required Dataset |
|:---:|---|:---:|---|:---:|
| **Exp 1** | [`exp01_numpy_scipy_pandas.py`](./exp01_numpy_scipy_pandas.py) | Python | NumPy, SciPy & Pandas package features and sample operations | In-memory |
| **Exp 2** | [`exp02_email_eda.py`](./exp02_email_eda.py) | Python | Exploratory Data Analysis (EDA) on Email dataset | `emails.csv` |
| **Exp 3** | [`exp03_weather_analysis.py`](./exp03_weather_analysis.py) | Python | NumPy statistics and weather data manipulation | `weather_2012.csv` |
| **Exp 4** | [`exp04_customer_feedback_cleaning.py`](./exp04_customer_feedback_cleaning.py)<br>*(R: [`exp04_customer_feedback_cleaning.R`](./exp04_customer_feedback_cleaning.R))* | Python / R | Data cleaning on messy customer feedback data | In-memory |
| **Exp 5** | [`exp05_student_performance_ggplot.py`](./exp05_student_performance_ggplot.py)<br>*(R: [`exp05_student_performance_ggplot.R`](./exp05_student_performance_ggplot.R))* | Python / R | Student test performance analysis and visualizations | In-memory |
| **Exp 6** | [`exp06_retail_sales_analysis.py`](./exp06_retail_sales_analysis.py) | Python | Retail store weekly sales exploration & analysis | In-memory |
| **Exp 7** | [`exp07_vaccination_data_visualization.py`](./exp07_vaccination_data_visualization.py) | Python | Indian states COVID-19 vaccination rates visualization | In-memory |
| **Exp 8** | [`exp08_wine_quality_eda.py`](./exp08_wine_quality_eda.py) | Python | Exploratory Data Analysis on Wine Quality dataset | `winequality-red.csv`<br>`winequality-white.csv` |
| **Exp 9** | [`exp09_pima_diabetes_univariate_analysis.py`](./exp09_pima_diabetes_univariate_analysis.py) | Python | Univariate analysis on Pima Indians Diabetes dataset | `Pima2.csv` |
| **Exp 10** | [`exp10_basemap_geographic_visualization.py`](./exp10_basemap_geographic_visualization.py) | Python | Visualizing geographic data with Basemap (Content Beyond Syllabus) | Basemap assets |

> For comprehensive lab record documentation with aims, procedures, sample outputs, and results, see [**FDS_LAB_PROGRAMS.md**](./FDS_LAB_PROGRAMS.md).

## Installation & Setup

Install required Python libraries:
```bash
pip install numpy scipy pandas matplotlib seaborn
```

For Experiment 10 (Basemap):
```bash
pip install pillow basemap basemap-data
```

## Running the Programs

Run any experiment directly with Python:
```bash
python exp01_numpy_scipy_pandas.py
python exp02_email_eda.py
python exp03_weather_analysis.py
python exp04_customer_feedback_cleaning.py
python exp05_student_performance_ggplot.py
python exp06_retail_sales_analysis.py
python exp07_vaccination_data_visualization.py
python exp08_wine_quality_eda.py
python exp09_pima_diabetes_univariate_analysis.py
python exp10_basemap_geographic_visualization.py
```

To run the original R scripts for Experiments 4 and 5:
```bash
Rscript exp04_customer_feedback_cleaning.R
Rscript exp05_student_performance_ggplot.R
```
