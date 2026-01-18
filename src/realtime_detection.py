import subprocess
import numpy as np
import joblib

# Load trained model and scaler
model = joblib.load("ssh_bruteforce_model.pkl")
scaler = joblib.load("scaler.pkl")

# Track IP behavior in real time
ip_fail_counts = {}
ip_frequency = {}

common_users = ["root", "admin", "ubuntu", "test"]

print("🔴 Real-time SSH ML Intrusion Detection Started")

# Follow SSH logs live
process = subprocess.Popen(
    ["journalctl", "-u", "ssh", "-f", "--no-pager"],
    stdout=subprocess.PIPE,
    text=True
)

for line in process.stdout:

    if "Failed password" in line or "Accepted password" in line:
        parts = line.split()

        if "from" not in parts:
            continue

        ip = parts[parts.index("from") + 1]
        hour = int(parts[2].split(":")[0])

        # Count failed attempts
        if "Failed password" in line:
            ip_fail_counts[ip] = ip_fail_counts.get(ip, 0) + 1
        else:
            ip_fail_counts[ip] = ip_fail_counts.get(ip, 0)

        # Track IP frequency
        ip_frequency[ip] = ip_frequency.get(ip, 0) + 1

        # Extract username
        username = parts[parts.index("for") + 1]
        is_common = 1 if username.lower() in common_users else 0

        # Build feature vector
        features = np.array([[
            ip_fail_counts[ip],
            hour,
            is_common,
            ip_frequency[ip]
        ]])

        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)[0]

        # Alerting
        if prediction == 1:
            print("🚨 ALERT: Possible SSH Brute Force from", ip)
        else:
            print("✔ Normal SSH activity from", ip)
