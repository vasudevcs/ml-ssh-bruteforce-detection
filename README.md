# ML SSH Brute Force Detection

This project is a simple machine learning–based system to detect SSH brute-force
login attempts on a Linux system.

It analyzes SSH authentication logs, extracts basic behavioral patterns, and uses
a machine learning model to classify login activity as normal or suspicious.

---

## What this project does

- Reads SSH authentication logs using `journalctl`
- Detects failed and successful SSH login attempts
- Extracts useful features such as:
  - Number of failed attempts from an IP address
  - Time of login attempt (hour of the day)
  - Use of common usernames (root, admin, etc.)
  - Frequency of IP addresses
- Trains a machine learning model to detect brute-force attacks
- Uses the trained model to monitor SSH logs in real time

---

## Machine Learning Used

- Algorithm: Logistic Regression
- Type: Binary classification (normal vs attack)

The model learns patterns from SSH login behavior to identify suspicious activity.

---

## How to Run (Linux)

Run the scripts in the following order:

```bash
python src/ssh_log_parser.py
python src/feature_engineering.py
python src/train_model.py
python src/realtime_detection.py
```
Notes
SSH logs are not included in this repository.

Generated datasets are created locally and ignored using .gitignore.

Trained model files are generated locally and not committed to GitHub.
