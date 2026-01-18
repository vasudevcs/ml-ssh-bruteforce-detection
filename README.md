# ML SSH Brute Force Detection

This project is a simple machine learning–based system to detect SSH brute-force
login attempts on a Linux system.

It analyzes SSH authentication logs, extracts useful patterns, and uses a
machine learning model to classify login behavior as normal or suspicious.

## What this project does
- Reads SSH authentication logs using `journalctl`
- Identifies failed and successful login attempts
- Extracts basic features such as:
  - Number of failed attempts from an IP
  - Login time (hour)
  - Use of common usernames
  - Frequency of an IP address
- Trains a machine learning model to detect brute-force attacks
- Applies the model to SSH logs in real time

## Machine Learning Used
- Algorithm: Logistic Regression
- Type: Binary classification (normal vs attack)

## Project Structure
ml-ssh-bruteforce-detection/
├── src/
│ ├── ssh_log_parser.py
│ ├── feature_engineering.py
│ ├── train_model.py
│ └── realtime_detection.py
├── data/
│ └── .gitkeep
├── models/
│ └── .gitkeep
├── .gitignore
├── requirements.txt
└── README.md


## How to Run (Linux)
python src/ssh_log_parser.py
python src/feature_engineering.py
python src/train_model.py
python src/realtime_detection.py

## Notes
- SSH logs and generated datasets are not included in this repository.
- Trained model files are generated locally and ignored using `.gitignore`.

## Author
Vasudev C S
