import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from specified path "csv file"
data_path = "/app/data/housing.csv"
data = pd.read_csv(data_path)

# Select features for clustering, column names in the CSV file
# Im using longitude and latitude as the data for clustering
features = ["longitude", "latitude"]  # Replace with actual column names

# Check if features exist in the data
if not all(feature in data.columns for feature in features):
    raise ValueError(f"Features {', '.join(features)} not found in data")

X = data[features]

# KMeans model and cluster labels (assuming fixed parameters)
kmeans = KMeans(n_clusters=4)  # Replace 3 with your desired number of clusters
kmeans.fit(X)
data["cluster_label"] = kmeans.labels_

# Create the plot
plt.figure(figsize=(8, 6))
sns.scatterplot(
    x=features[0], y=features[1], hue="cluster_label", data=data, palette="Set3"
)
plt.title("K-Means Clustering")
plt.xlabel(features[0])
plt.ylabel(features[1])
plt.tight_layout()

# Save the plot with desired path
save_path = "/app/data/kmeans_plot.png"  # Replace with your desired filename
plt.savefig(save_path)

print(f"K-Means clustering plot saved as: {save_path}")
