import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

print("🧠 Training AI to detect attacks...")

# Load the logs
df = pd.read_csv("network_logs.csv")

# Create a simple feature: suspicious IPs
suspicious_ips = ["203.0.113.5", "198.51.100.7"]
df["Is_Suspicious_IP"] = df["Source_IP"].apply(lambda x: 1 if x in suspicious_ips else 0)

# Features and target
X = df[["Is_Suspicious_IP"]]
y = df["Is_Attack"]

# Train the model
model = RandomForestClassifier()
model.fit(X, y)

# Save the model
joblib.dump(model, "attack_model.pkl")

print("✅ Model trained and saved as 'attack_model.pkl'")
print(f"🎯 Model accuracy: {model.score(X, y) * 100:.2f}%")