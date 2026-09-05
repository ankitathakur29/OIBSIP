# Customer Segmentation Analysis

## Project Overview
This project performs Customer Segmentation using the K-Means Clustering algorithm.

The customers are grouped based on their purchasing behavior using RFM Analysis:

- Recency: Number of days since the customer's last purchase.
- Frequency: Number of purchases made by the customer.
- Monetary: Total amount spent by the customer.

## Dataset
The dataset used for this project is the Online Retail dataset.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## Steps Performed
1. Loaded the Online Retail dataset.
2. Cleaned missing values.
3. Converted InvoiceDate into datetime format.
4. Created the TotalPrice column.
5. Performed RFM Analysis.
6. Standardized the RFM features.
7. Used the Elbow Method to find the optimal number of clusters.
8. Applied K-Means Clustering.
9. Divided customers into 4 clusters.
10. Visualized customer segments.

## Customer Segments

### Cluster 0 - Regular Customers
Customers with regular purchasing behavior.

### Cluster 1 - Inactive Customers
Customers with low frequency and long recency.

### Cluster 2 - VIP Customers
Customers with very high spending and purchase frequency.

### Cluster 3 - High-Value Customers
Customers with high purchase frequency and high spending.

## Results
The analysis successfully divided customers into 4 different clusters based on their purchasing behavior.

## Author
Ankita Gautam
