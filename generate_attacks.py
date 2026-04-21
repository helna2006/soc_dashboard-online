import pandas as pd
import random
from datetime import datetime, timedelta

print("🔐 Generating simulated attack logs...")

# List of possible IP addresses
ips = ["192.168.1.1", "192.168.1.2", "10.0.0.5", "172.16.0.3", "203.0.113.5", "198.51.100.7"]

# Attack types
attack_types = ["Normal", "Brute Force", "Port Scan", "Malicious Payload"]

data = []
start_time = datetime.now()

for i in range(1000):
    ip = random.choice(ips)
    attack = random.choices(attack_types, weights=[0.7, 0.1, 0.1, 0.1])[0]
    timestamp = start_time - timedelta(seconds=i*10)
    
    data.append([ip, attack, timestamp, 1 if attack != "Normal" else 0])

df = pd.DataFrame(data, columns=["Source_IP", "Attack_Type", "Timestamp", "Is_Attack"])
df.to_csv("network_logs.csv", index=False)

print("✅ Done! Created 'network_logs.csv' with 1000 log entries.")
print(df.head())