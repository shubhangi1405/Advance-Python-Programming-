import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Dataset
df = pd.read_csv("customer_churn.csv")

print("First 5 Rows:")
print(df.head())

# 2. Dataset Information
print("\nDataset Information:")
print(df.info())

# 3. Descriptive Statistics
print("\nDescriptive Statistics:")
print(df.describe())

# 4. Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle Missing Values
df = df.dropna()

# 5. Detect and Remove Outliers using IQR
col = 'MonthlyCharges'

Q1 = df[col].quantile(0.25)
Q3 = df[col].quantile(0.75)
IQR = Q3 - Q1

df = df[(df[col] >= Q1 - 1.5 * IQR) &
        (df[col] <= Q3 + 1.5 * IQR)]

print("\nCleaned Data:")
print(df.head())

# 6. Data Visualization

# Churn Count
sns.countplot(x='Churn', data=df)
plt.title("Customer Churn Count")
plt.show()

# Monthly Charges Distribution
sns.histplot(df['MonthlyCharges'], kde=True)
plt.title("Monthly Charges Distribution")
plt.show()

# Outlier Detection
sns.boxplot(x=df['MonthlyCharges'])
plt.title("Monthly Charges Outliers")
plt.show()

# 7. Churn Analysis
print("\nChurn Analysis:")
print(df['Churn'].value_counts())

print("\nAverage Monthly Charges:")
print(df['MonthlyCharges'].mean())
