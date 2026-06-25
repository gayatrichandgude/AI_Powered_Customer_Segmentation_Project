import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import joblib

# Load dataset
df = pd.read_csv("dataset/customers.csv")

# Features
X = df[["Age", "AnnualIncome", "SpendingScore"]]

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-Means
kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

df["Segment"] = kmeans.fit_predict(X_scaled)

# Save model
joblib.dump(kmeans, "model/kmeans_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")

# Save segmented data
df.to_csv(
    "dataset/customer_segments.csv",
    index=False
)

print("Model Trained Successfully")
print(df.head())