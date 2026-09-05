import pandas as pd

# Load the dataset
df = pd.read_csv("online_retail.csv")

# Show first 5 rows
print(df.head())

# Show dataset information
print(df.info())
# Check missing values
print("\nMissing Values:")
#print(df.isnull().sum())

# Remove rows with missing CustomerID
df = df.dropna(subset=["CustomerID"])

# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Create TotalPrice column
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

print("\nDataset after cleaning:")
print(df.info())
# Find the latest date in the dataset
reference_date = df["InvoiceDate"].max()

# Create RFM table
rfm = df.groupby("CustomerID").agg({
    "InvoiceDate": lambda x: (reference_date - x.max()).days,
    "InvoiceNo": "nunique",
    "TotalPrice": "sum"
})

# Rename columns
rfm.columns = ["Recency", "Frequency", "Monetary"]

# Show first 5 customers
print("\nRFM Analysis:")
print(rfm.head())

# Show RFM statistics
print("\nRFM Statistics:")
print(rfm.describe())
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
# Remove customers with negative or zero monetary value
rfm_clean = rfm[rfm["Monetary"] > 0].copy()

print("\nRFM Data after removing negative values:")
print(rfm_clean.describe())

# Select features for clustering
features = rfm_clean[["Recency", "Frequency", "Monetary"]]

# Standardize the data
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

print("\nData is ready for K-Means Clustering!")
# Create K-Means model with 4 customer clusters
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)

# Train the model
rfm_clean["Cluster"] = kmeans.fit_predict(scaled_features)

# Show first 5 customers with their cluster
#sprint("\nCustomer Clusters:")
print(rfm_clean.head())

# Count customers in each cluster
print("\nNumber of Customers in Each Cluster:")
print(rfm_clean["Cluster"].value_counts().sort_index())
# Standardize the RFM values
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

scaler = StandardScaler()

rfm_scaled = scaler.fit_transform(
    rfm_clean[["Recency", "Frequency", "Monetary"]]
)

print("\nData is standardized successfully!")
print("\nCluster Summary:")

cluster_summary = rfm_clean.groupby("Cluster")[["Recency", "Frequency", "Monetary"]].mean()

print(cluster_summary)
import matplotlib.pyplot as plt

# Customer count in each cluster
rfm_clean["Cluster"].value_counts().sort_index().plot(
    kind="bar"
)

plt.title("Number of Customers in Each Cluster")
plt.xlabel("Cluster")
plt.ylabel("Number of Customers")
plt.show()
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

plt.scatter(
    rfm_clean["Recency"],
    rfm_clean["Monetary"],
    c=rfm_clean["Cluster"]
)

plt.xlabel("Recency")
plt.ylabel("Monetary")
plt.title("Customer Segmentation: Recency vs Monetary")

plt.show()
# Customer Segment Names
cluster_names = {
    0: "Regular Customers",
    1: "Inactive Customers",
    2: "VIP Customers",
    3: "High-Value Customers"
}

rfm_clean["Customer Segment"] = rfm_clean["Cluster"].map(cluster_names)

print("\nCustomer Segments:")
print(rfm_clean[["Recency", "Frequency", "Monetary", "Cluster", "Customer Segment"]].head())
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

plt.scatter(
    rfm_clean["Frequency"],
    rfm_clean["Monetary"],
    c=rfm_clean["Cluster"],
    cmap="viridis"
)

plt.title("Customer Segmentation: Frequency vs Monetary")
plt.xlabel("Frequency")
plt.ylabel("Monetary")

plt.show()
inertia = []

for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(rfm_scaled)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), inertia, marker='o')

plt.title("Elbow Method for Optimal Clusters")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")

plt.show()
print("\nCustomer Segmentation Analysis Completed Successfully!")

print("\nFinal Insights:")
print("1. Customers were divided into 4 different clusters.")
print("2. Cluster 0 represents regular customers.")
print("3. Cluster 1 represents inactive or low-value customers.")
print("4. Cluster 2 represents VIP customers with very high spending.")
print("5. Cluster 3 represents high-value frequent customers.")
