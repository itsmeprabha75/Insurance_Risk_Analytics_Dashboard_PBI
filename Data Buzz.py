# Preprocessing And EDA of Insurance_Dataset
# 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Load Dataset
df1 = pd.read_csv(r"C:/Users/91951/Downloads/Data Buzz/Insurance_Dataset.csv")
df2 = pd.read_csv(r"C:/Users/91951/Downloads/Data Buzz/Dim_Driving.csv")
df3 = pd.read_csv(r"C:/Users/91951/Downloads/Data Buzz/Dim_Health.csv")
df4 = pd.read_csv(r"C:/Users/91951/Downloads/Data Buzz/Dim_Customer.csv")

Insurance_Dataset_Raw = pd.concat([df1, df2, df3,df4], ignore_index=True)
# 3. Basic Info
print("Initial Dataset Shape:", Insurance_Dataset_Raw.shape)
print("\nData Types:\n", Insurance_Dataset_Raw.dtypes)
print("\n1st 5 rows of dataset:\n",Insurance_Dataset_Raw.head())
print("\nlast 5 rows of dataset:\n",Insurance_Dataset_Raw.tail())
print("\nbasic info of dataset:\n",Insurance_Dataset_Raw.info())
print("\nStatistics of dataset:\n",Insurance_Dataset_Raw.describe(include="all"))

Insurance_Dataset_Clean = Insurance_Dataset_Raw.copy()
# 4. Standardize column names
Insurance_Dataset_Clean.columns = (
    Insurance_Dataset_Clean.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# 5. Separate Numerical & Categorical Columns
# Numerical columns
numerical_columns = Insurance_Dataset_Clean.select_dtypes(include=np.number).columns.tolist()
# Categorical columns (only object or category types)
categorical_columns = Insurance_Dataset_Clean.select_dtypes(include=["object", "category"]).columns.tolist()
# Datetime columns
datetime_columns = Insurance_Dataset_Clean.select_dtypes(include=["datetime64[ns]", "datetimetz"]).columns.tolist()

print("Numerical:", numerical_columns)
print("Categorical:", categorical_columns)
print("Datetime:", datetime_columns)

# 6. Handling Duplicate
Insurance_Dataset_Clean.duplicated().sum()

# 9. Handling Missing Values
Insurance_Dataset_Clean.isnull().sum()

# 10. OutlierDetection 
for i, col in enumerate(numerical_columns):
    Q1 = Insurance_Dataset_Clean[col].quantile(0.25)
    Q3 = Insurance_Dataset_Clean[col].quantile(0.75)
    IQR = Q3 - Q1
    outliers = Insurance_Dataset_Clean[(Insurance_Dataset_Clean[col] < (Q1 - 1.5 * IQR)) | (Insurance_Dataset_Clean[col] > (Q3 + 1.5 * IQR))]
    print(f"Outliers detected in {col}:\n", outliers[col])
    plt.figure(figsize=(6,4))
    sns.boxplot(y=Insurance_Dataset_Clean[col])
    plt.title(f"Boxplot of {col}")
    plt.show()
    
Insurance_Dataset_EDA = Insurance_Dataset_Clean.copy()
# 11.  Correlation Analysis
corr_matrix = Insurance_Dataset_EDA[numerical_columns].corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

#pair plot
sns.pairplot(Insurance_Dataset_EDA[numerical_columns], diag_kind="kde", plot_kws={'alpha':0.5})
plt.suptitle("Pairplot of Numerical Variables", y=1.02)
plt.show()

