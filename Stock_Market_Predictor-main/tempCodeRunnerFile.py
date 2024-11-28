import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the Dataset
data = pd.read_csv('your_dataset.csv')

# Step 2: Descriptive Statistics
print("Descriptive Statistics:")
print(data.describe())

# Step 3: Check for Missing Data
missing_data = data.isnull().sum()
print("\nMissing Data:\n", missing_data)

# Step 4: Handle Missing Data (Example: Filling missing values with the mean)
data.fillna(data.mean(), inplace=True)

# Step 5: Visualize Data
plt.figure(figsize=(12, 6))

# Histogram for data distribution
plt.subplot(2, 2, 1)
sns.histplot(data['PM2.5'], kde=True, color='blue')
plt.title('PM2.5 Distribution')

# Box plot for identifying outliers in PM2.5
plt.subplot(2, 2, 2)
sns.boxplot(data['PM2.5'], color='green')
plt.title('PM2.5 Outliers')

# Scatter plot for relationship between PM2.5 and NO2
plt.subplot(2, 2, 3)
plt.scatter(data['PM2.5'], data['NO2'], color='purple')
plt.title('PM2.5 vs NO2')

plt.tight_layout()
plt.show()

# Step 6: Detect Outliers using IQR method
Q1 = data['PM2.5'].quantile(0.25)
Q3 = data['PM2.5'].quantile(0.75)
IQR = Q3 - Q1

# Outliers are values below Q1 - 1.5 * IQR or above Q3 + 1.5 * IQR
outliers = data[(data['PM2.5'] < (Q1 - 1.5 * IQR)) | (data['PM2.5'] > (Q3 + 1.5 * IQR))]
print("\nOutliers:\n", outliers)

# Removing outliers from the dataset (optional)
data_no_outliers = data[~((data['PM2.5'] < (Q1 - 1.5 * IQR)) | (data['PM2.5'] > (Q3 + 1.5 * IQR)))]
