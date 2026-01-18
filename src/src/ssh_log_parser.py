import csv
import subprocess
from datetime import datetime

THRESHOLD = 5
YEAR = datetime.now().year

failed_count = 0
success_count = 0
ip_fail_counts = {}
dataset = []

MONTH_MAP = {
    "jan":"01","feb":"02","mar":"03","apr":"04",
    "may":"05","jun":"06","jul":"07","aug":"08",
    "sep":"09","oct":"10","nov":"11","dec":"12"
}

logs = subprocess.check_output(
    ["journalctl", "-u", "ssh", "--no-pager"],
    text=True
)

for line in logs.splitlines():
    parts = line.split()

    if "Failed password" in line:
        failed_count += 1

        month = parts[0].lower()[:3]
        day = parts[1]
        time = parts[2]
        timestamp = f"{YEAR}-{MONTH_MAP[month]}-{day} {time}"

        if "from" not in parts:
            continue
        ip = parts[parts.index("from") + 1]

        if "invalid user" in line:
            username = parts[parts.index("user") + 1]
        else:
            username = parts[parts.index("for") + 1]

        ip_fail_counts[ip] = ip_fail_counts.get(ip, 0) + 1
        failed_attempts = ip_fail_counts[ip]

        label = 1 if failed_attempts >= THRESHOLD else 0

        dataset.append([timestamp, ip, username, failed_attempts, label])

    elif "Accepted password" in line:
        success_count += 1

        month = parts[0].lower()[:3]
        day = parts[1]
        time = parts[2]
        timestamp = f"{YEAR}-{MONTH_MAP[month]}-{day} {time}"

        if "from" not in parts:
            continue
        ip = parts[parts.index("from") + 1]
        username = parts[parts.index("for") + 1]

        dataset.append([timestamp, ip, username, 0, 0])

with open("ssh_login_dataset.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "timestamp", "ip_address", "username",
        "failed_attempt_count", "label"
    ])
    writer.writerows(dataset)

print("Dataset created successfully")
print("Failed logins:", failed_count)
print("Successful logins:", success_count)
