import pandas as pd

# Load dataset
file = pd.read_csv("WindPower.csv")

# Show first 5 rows
print("First 5 Rows")
print(file.head())

# Dataset shape
print("\nDataset Shape")
print(file.shape)

# Column names
print("\nColumn Names")
print(file.columns)

# Information about dataset
print("\nDataset Information")
print(file.info())

# Check null values
print("\nMissing Values")
print(file.isnull().sum())

# Statistical summary
print("\nStatistical Summary")
print(file.describe())

# Check duplicate rows
print("\nDuplicate Rows")
print(file.duplicated().sum())
