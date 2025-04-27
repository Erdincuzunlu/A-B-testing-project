# A/B Testing - Control Group vs Test Group
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import norm, shapiro, uniform, levene, ttest_ind

# Data load
file_path = '/Users/erdinc/PycharmProjects/pythonProject3/New Project/ab_testing.xlsx'
excel_file = pd.ExcelFile(file_path)

# Check sheet names
print("Sheet Names:", excel_file.sheet_names)

# Read control and test groups separately
control_df = pd.read_excel(file_path, sheet_name='Control Group')
test_df = pd.read_excel(file_path, sheet_name='Test Group')

# Quick overview
print("\nControl Group Head:")
print(control_df.head())
print("\nTest Group Head:")
print(test_df.head())

# Shape and info
print("\nControl Group Shape:", control_df.shape)
print("Test Group Shape:", test_df.shape)
print("\nControl Group Info:")
print(control_df.info())
print("\nTest Group Info:")
print(test_df.info())

# Combine datasets if needed (not mandatory for A/B testing)
full_df = pd.concat([control_df, test_df], ignore_index=True)

# Hypotheses
# H0: M1 = M2 (The mean of the Control Group and the Test Group is equal)
# H1: M1 ≠ M2 (The mean of the Control Group and the Test Group is different)

# Mean Purchase Values
print("\nControl Group Purchase Mean:", control_df["Purchase"].mean())
print("Test Group Purchase Mean:", test_df["Purchase"].mean())

# Normality Test - Shapiro-Wilk
stat_control, p_control = shapiro(control_df["Purchase"])
stat_test, p_test = shapiro(test_df["Purchase"])

print("\nNormality Test (Shapiro-Wilk):")
print(f"Control Group p-value: {p_control}")
print(f"Test Group p-value: {p_test}")

# Variance Homogeneity Test - Levene Test
stat_levene, p_levene = levene(control_df["Purchase"], test_df["Purchase"])
print("\nVariance Homogeneity Test (Levene):")
print(f"Levene p-value: {p_levene}")

# Independent Samples T-Test (equal variance assumed)
test_stat, p_value = ttest_ind(control_df["Purchase"], test_df["Purchase"], equal_var=True)

print("\nIndependent Samples T-Test Result:")
print(f"Test Statistic: {test_stat}")
print(f"P-Value: {p_value}")

# Conclusion
if p_value < 0.05:
    print("\nResult: There is a statistically significant difference between the groups (Reject H0).")
else:
    print("\nResult: There is no statistically significant difference between the groups (Fail to reject H0).")