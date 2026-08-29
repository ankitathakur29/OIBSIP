import pandas as pd

df = pd.read_csv("retail_sales_dataset.csv")

print(df.head())
print(df.info())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nBasic Statistics:")
print(df.describe())

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

print("\nDate Information:")
print("Start Date:", df["Date"].min())
print("End Date:", df["Date"].max())

print("\nProduct Category Sales:")
print(df.groupby("Product Category")["Total Amount"].sum())

print("\nGender-wise Sales:")
print(df.groupby("Gender")["Total Amount"].sum())

print("\nTop 10 Customers by Sales:")
print(
    df.groupby("Customer ID")["Total Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print("\nDetailed Descriptive Statistics:")

numeric_columns = [
    "Age",
    "Quantity",
    "Price per Unit",
    "Total Amount"
]

for column in numeric_columns:
    print(f"\n{column}:")
    print("Mean:", df[column].mean())
    print("Median:", df[column].median())
    print("Mode:", df[column].mode()[0])
    print("Standard Deviation:", df[column].std())
    # Create Year-Month column
df["Month"] = df["Date"].dt.to_period("M")

# Monthly Sales
monthly_sales = df.groupby("Month")["Total Amount"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# Quarterly Sales
quarterly_sales = df.groupby(df["Date"].dt.to_period("Q"))["Total Amount"].sum()

print("\nQuarterly Sales:")
print(quarterly_sales)
import matplotlib.pyplot as plt

# Monthly Sales Trend
plt.figure(figsize=(12, 5))
plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Quarterly Sales Trend
plt.figure(figsize=(10, 5))
plt.plot(quarterly_sales.index.astype(str), quarterly_sales.values, marker="o")
plt.title("Quarterly Sales Trend")
plt.xlabel("Quarter")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Age Group Analysis

bins = [0, 18, 25, 35, 45, 55, 100]
labels = ["Under 18", "18-25", "26-35", "36-45", "46-55", "56+"]

df["Age Group"] = pd.cut(
    df["Age"],
    bins=bins,
    labels=labels,
    include_lowest=True
)

print("\nAge Group Distribution:")
print(df["Age Group"].value_counts().sort_index())

print("\nAge Group Sales:")
print(df.groupby("Age Group", observed=False)["Total Amount"].sum())
# Age Group Sales Chart

age_group_sales = df.groupby(
    "Age Group",
    observed=False
)["Total Amount"].sum()

plt.figure(figsize=(10, 5))
age_group_sales.plot(kind="bar")
plt.title("Sales by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# Gender-wise Sales Chart

gender_sales = df.groupby("Gender")["Total Amount"].sum()

plt.figure(figsize=(8, 5))
gender_sales.plot(kind="bar")
plt.title("Sales by Gender")
plt.xlabel("Gender")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# Product Category Analysis

category_sales = df.groupby("Product Category")["Total Amount"].sum().sort_values(
    ascending=False
)

print("\nRevenue by Product Category:")
print(category_sales)

# Product Category Sales Chart
plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")

plt.title("Revenue by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Revenue")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# Correlation Heatmap

import seaborn as sns

numeric_data = df[
    ["Age", "Quantity", "Price per Unit", "Total Amount"]
]

correlation_matrix = numeric_data.corr()

print("\nCorrelation Matrix:")
print(correlation_matrix)

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
# Additional Visualization:
# Average Transaction Amount by Gender

average_gender_sales = df.groupby("Gender")["Total Amount"].mean().sort_values(
    ascending=False
)

print("\nAverage Transaction Amount by Gender:")
print(average_gender_sales)

plt.figure(figsize=(8, 5))
average_gender_sales.plot(kind="bar")

plt.title("Average Transaction Amount by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Transaction Amount")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()