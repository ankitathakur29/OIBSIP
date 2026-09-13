# Data Cleaning on Cafe Sales Data

## Project Overview

This project focuses on cleaning and preparing a cafe sales dataset for further data analysis and visualization.

## Dataset

The dataset contains 10,000 transaction records and 8 columns related to cafe sales.

Columns include:
- Transaction ID
- Item
- Quantity
- Price Per Unit
- Total Spent
- Payment Method
- Location
- Transaction Date

## Data Cleaning Performed

- Handled missing values.
- Replaced invalid and unknown values.
- Converted numerical columns into appropriate numeric data types.
- Converted Transaction Date into datetime format.
- Checked and removed duplicate rows.
- Detected outliers using the IQR method.
- Capped outliers in Total Spent using the IQR method.

## Final Dataset

- Rows: 10,000
- Columns: 8
- Missing Values: 0
- Duplicate Rows: 0

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

## Conclusion

The data cleaning process successfully transformed the raw cafe sales dataset into a clean and consistent dataset. The cleaned dataset is suitable for further data analysis and visualization.
