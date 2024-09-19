import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
data_path = "C:\Users\hp\Desktop\Dia 1\diabetes (1).csv" # Adjust path as needed
diabetes_data = pd.read_csv(data_path)

# Task 2: Print the first 10 rows of the dataframe
print("First 10 rows of the dataframe:")
print(diabetes_data.head(10))

# Task 3: Print the information about the data types, columns, null value counts, memory consumption
print("\nDataframe Information:")
diabetes_data.info()

# Task 4: Print basic statistical details about the data
print("\nStatistical details of the dataframe:")
print(diabetes_data.describe())

# Task 5: Print basic statistical details about the data by reversing the axes
print("\nStatistical details by reversing the axes:")
print(diabetes_data.describe().T)

# Task 6: Treat zero values as missing values and replace them with NaN
columns_with_zeros = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
diabetes_data[columns_with_zeros] = diabetes_data[columns_with_zeros].replace(0, np.nan)

# Task 7: Plot the data distribution for each column
print("\nPlotting data distribution for each column before filling missing values:")
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 10))
for idx, column in enumerate(diabetes_data.columns):
    ax = axes.flatten()[idx]
    diabetes_data[column].hist(ax=ax)
    ax.set_title(column)
plt.tight_layout()
plt.show()

# Task 8: Fill in the NaN values for the columns using the median
for column in columns_with_zeros:
    median_value = diabetes_data[column].median()
    diabetes_data.loc[:, column] = diabetes_data[column].fillna(median_value)


# Task 9: Plot the data distribution after filling in the missing data
print("\nPlotting data distribution for each column after filling missing values:")
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 10))
for idx, column in enumerate(diabetes_data.columns):
    ax = axes.flatten()[idx]
    diabetes_data[column].hist(ax=ax)
    ax.set_title(column)
plt.tight_layout()
plt.show()
