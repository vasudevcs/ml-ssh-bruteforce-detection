import pandas as pd

# Load raw dataset
df = pd.read_csv("ssh_login_dataset.csv")

# Extract hour of login (attacks often happen at odd hours)
df["hour_of_the_day"] = (
    df["timestamp"]
    .str.split(" ", expand=True)[1]
    .str.split(":", expand=True)[0]
    .astype(int)
)

# Check if attacker used common usernames
common_users = ["root", "admin", "ubuntu", "test"]
df["is_common_username"] = df["username"].str.lower().isin(common_users).astype(int)

# Count how often each IP appears
df["ip_frequency"] = df["ip_address"].map(
    df["ip_address"].value_counts()
)

# Save cleaned dataset
df.to_csv("clean_dataset.csv", index=False)

print("Feature engineering completed")
