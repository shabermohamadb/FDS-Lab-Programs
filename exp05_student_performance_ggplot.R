# EXPERIMENT 5
# Title: PERFORM ANALYSIS AND VISUALIZATIONS ON STUDENT TEST PERFORMANCE DATA USING GGPLOT
# Aim: To perform various analysis and visualization on student test performance using ggplot features.

student_data <- data.frame(
  Gender = sample(c("Male", "Female"), 100, replace = TRUE),
  Math_Score = rnorm(100, mean = 65, sd = 15),
  Reading_Score = rnorm(100, mean = 70, sd = 10),
  Writing_Score = rnorm(100, mean = 68, sd = 12),
  Prep_Course = sample(c("Completed", "None"), 100, replace = TRUE)
)
print("--- Student Performance Data Head ---")
print(head(student_data))

library(ggplot2)

# 1. Distribution of Math Scores
p1 <- ggplot(student_data, aes(x = Math_Score)) +
  geom_histogram(binwidth = 5, fill = "steelblue", color = "black") +
  theme_minimal() +
  labs(title = "Distribution of Math Scores", x = "Math Score", y = "Count")
print(p1)

# 2. Math Scores by Gender (Boxplot)
p2 <- ggplot(student_data, aes(x = Gender, y = Math_Score, fill = Gender)) +
  geom_boxplot() +
  theme_minimal() +
  labs(title = "Math Scores by Gender", x = "Gender", y = "Math Score")
print(p2)

# 3. Reading Scores by Prep Course (Violin Plot)
p3 <- ggplot(student_data, aes(x = Prep_Course, y = Reading_Score, fill = Prep_Course)) +
  geom_violin(trim = FALSE) +
  theme_minimal() +
  labs(title = "Reading Scores by Test Prep Course", x = "Test Preparation Course", y = "Reading Score")
print(p3)

# 4. Math vs Reading Scores by Gender (Scatter Plot)
p4 <- ggplot(student_data, aes(x = Math_Score, y = Reading_Score, color = Gender)) +
  geom_point(alpha = 0.7) +
  theme_minimal() +
  labs(title = "Math vs Reading Scores", x = "Math Score", y = "Reading Score")
print(p4)

# 5. Average Score Calculation and Boxplot
student_data$Average_Score <- rowMeans(student_data[, c("Math_Score", "Reading_Score", "Writing_Score")])

p5 <- ggplot(student_data, aes(x = Prep_Course, y = Average_Score, fill = Prep_Course)) +
  geom_boxplot() +
  theme_minimal() +
  labs(title = "Average Scores by Test Preparation Course", x = "Test Preparation", y = "Average Score")
print(p5)

cat("\\nResult: Thus, the R programs were written and executed to perform analysis and visualization on student test performance data using ggplot features.\\n")
