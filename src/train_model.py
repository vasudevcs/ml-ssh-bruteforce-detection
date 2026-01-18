import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib

# Load cleaned dataset
df = pd.read_csv("clean_dataset.csv")

# Select features and label
X = df[
    [
        "failed_attempt_count",
        "hour_of_the_day",
        "is_common_username",
        "ip_frequency"
    ]
]
y = df["label"]

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Scale features (important for Logistic Regression)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train ML model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# Evaluate model
y_pred = model.predict(X_test_scaled)
print(classification_report(y_test, y_pred))

# Save model and scaler
joblib.dump(model, "ssh_bruteforce_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("Model training completed and files saved")
