Early Detection of Diabetes - Data Cleansing and Exploration

Objective

The goal of this project is to explore a healthcare dataset and perform data cleansing using the Pandas library in Python. The dataset consists of medical variables related to diabetes, with the aim of deriving insights to support early detection. This project focuses on data cleaning and exploration but does not yet involve machine learning.
Background

Diabetes is increasing rapidly worldwide, and early detection can help prevent or delay the onset by taking appropriate measures. There is a need for easy, rapid, and accurate diagnostic tools for early diagnosis. While machine learning can assist in this, this project focuses on data cleansing as a foundational step.
Dataset

The dataset includes several independent variables:
Number of pregnancies
BMI
Insulin levels
Age
Glucose
BloodPressure
SkinThickness
Outcome (Target Variable: 0 for non-diabetic, 1 for diabetic)
Tasks

1. Data Loading
Read the diabetes.csv file into a Pandas DataFrame.
2. Initial Data Exploration
Print the first 10 rows of the dataset.
Print basic information about the dataset, including data types, column names, null value counts, and memory consumption.
Print basic statistical details for the dataset.
3. Data Transformation
Reverse the axes of the dataset to transpose the data (i.e., write rows as columns and vice-versa).
4. Handling Missing Values
Identify and replace zero values (which are invalid for certain columns) with NaN in the following columns:
Glucose
BloodPressure
SkinThickness
Insulin
BMI
Fill in the NaN values using an appropriate strategy based on the distribution of each column.
5. Data Visualization
Plot the data distribution for each column to understand the missing values and the overall structure.
Plot the data distribution again after filling in the missing values to assess the impact of the changes.
Installation

Clone the repository:
bash
Copy code
git clone https://github.com/your-username/diabetes-data-exploration.git
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Usage

Load the dataset by running the script:
bash
Copy code
python diabetes_data_cleaning.py
Follow the printed output to see the data cleansing steps and visualizations.
Results

Explore the cleaned data, observe how missing values were handled, and visualize the corrected distributions for all variables.
Requirements

Python 3.x
pandas
NumPy
matplotlib
seaborn
