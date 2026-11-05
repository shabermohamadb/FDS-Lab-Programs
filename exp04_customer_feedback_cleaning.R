# EXPERIMENT 4
# Title: DATA CLEANING ON MESSY CUSTOMER FEEDBACK DATA USING R
# Aim: To explore various variable and column filters in R for cleaning messy customer feedback data.

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
print("--- Raw Input DataFrame ---")
print(feedback_df)

# Step 2: Rename column CustomerID to Customer_ID
feedback_df <- feedback_df %>%
  rename(Customer_ID = CustomerID)

# Step 3: Text cleaning on Feedback column
feedback_df <- feedback_df %>%
  mutate(
    Feedback = str_trim(Feedback),
    Feedback = str_to_sentence(Feedback),
    Feedback = str_replace_all(Feedback, "[^[:alnum:] ]", "")
  )

# Step 4: Standardize and normalize Gender column
feedback_df <- feedback_df %>%
  mutate(
    Gender = str_to_lower(Gender),
    Gender = case_when(
      Gender %in% c("male", "m") ~ "Male",
      Gender %in% c("female", "f") ~ "Female",
      TRUE ~ "Other"
    )
  )
print("--- After Cleaning Feedback & Gender ---")
print(feedback_df)

# Step 5: Filter out missing Customer_ID records
feedback_df <- feedback_df %>%
  filter(!is.na(Customer_ID))
print("--- After Filter Non-NA Customer_ID ---")
print(feedback_df)

# Step 6: Filter out NA and blank Feedback records
feedback_df <- feedback_df %>%
  filter(!is.na(Feedback) & Feedback != "")
print("--- After Filter Non-Empty Feedback ---")
print(feedback_df)

# Step 7: Filter records where Rating is not NA and Rating >= 3
feedback_df <- feedback_df %>%
  filter(!is.na(Rating) & Rating >= 3)
print("--- After Filter Rating >= 3 ---")
print(feedback_df)

cat("\\nResult: Thus, the R programs were written and executed to explore various variable and column filters in messy customer feedback data.\\n")
