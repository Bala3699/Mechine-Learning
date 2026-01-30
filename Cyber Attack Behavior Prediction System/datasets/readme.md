---

# Cybersecurity 🪪 Intrusion 🦠 Detection Dataset
---
**Prevent Before Attack**

## Overview

This dataset is designed for detecting cyber intrusions based on network traffic and user behavior. It contains **9,537 records** with **10 features** for intrusion detection, including session information, network attributes, user behavior, and a binary attack detection label.

This dataset is ideal for building a **Machine Learning–Based Cyber Attack Behavior Prediction System**, such as the project developed during my **Blue Team internship**, where the goal was to **detect and predict cyber attacks in real time**.

---

## Dataset Structure

| Column Name           | Description                                                             |
| --------------------- | ----------------------------------------------------------------------- |
| `session_id`          | Unique identifier for each session                                      |
| `network_packet_size` | Size of network packets in bytes (64–1500 bytes)                        |
| `protocol_type`       | Protocol used: TCP, UDP, ICMP                                           |
| `encryption_used`     | Encryption protocol: AES, DES, None                                     |
| `login_attempts`      | Number of login attempts                                                |
| `session_duration`    | Session length in seconds                                               |
| `failed_logins`       | Number of failed login attempts                                         |
| `unusual_time_access` | Binary flag indicating login at unusual times (0 = normal, 1 = unusual) |
| `ip_reputation_score` | Score from 0 to 1 indicating suspicious activity                        |
| `browser_type`        | Browser used: Chrome, Firefox, Edge, Safari, Unknown                    |
| `attack_detected`     | Target variable: 1 = attack detected, 0 = normal activity               |

---

## Features Explained

### 1. Network-Based Features

* **network_packet_size:**

  * Lower values (~64 bytes) may indicate control messages.
  * Larger packets (~1500 bytes) often carry bulk data.
  * Abnormal sizes may indicate reconnaissance or attacks.

* **protocol_type:**

  * TCP: Reliable, connection-oriented.
  * UDP: Faster, less reliable (used for streaming).
  * ICMP: Used for diagnostics; may indicate DoS attacks.

* **encryption_used:**

  * AES: Strong encryption, commonly used.
  * DES: Older encryption, weaker security.
  * None: Unencrypted communication, risky for attacks.

### 2. User Behavior-Based Features

* **login_attempts:** High values may indicate brute-force attacks.
* **session_duration:** Very long sessions may indicate unauthorized access.
* **failed_logins:** High counts suggest credential stuffing or dictionary attacks.
* **unusual_time_access:** Binary flag; attackers often operate outside normal hours.
* **ip_reputation_score:** Higher values indicate suspicious IP addresses (botnets, spam, prior attacks).
* **browser_type:** Unknown browsers may indicate automated scripts or bots.

---

## Target Variable

* **attack_detected (Binary):**

  * `1` → Attack detected
  * `0` → Normal activity

This allows for **supervised machine learning** approaches for intrusion detection.

---

## Use Cases

### A. Machine Learning-Based Intrusion Detection

**Supervised Learning:**

* Models: Logistic Regression, Decision Trees, Random Forest, XGBoost, SVM
* Deep Learning: DNN, LSTM, CNN for pattern recognition
* Evaluate using accuracy, precision, recall, F1-score

**Deep Learning for Time-Series:**

* LSTM models for analyzing sequential network traffic

### B. Anomaly Detection (Unsupervised Learning)

* **Autoencoders:** Learn normal traffic, flag anomalies
* **Isolation Forest:** Detect outliers based on feature isolation
* **One-Class SVM:** Learn normal behavior and detect deviations

### C. Rule-Based Detection

* Example: Trigger an alert if `failed_logins > 10` **AND** `ip_reputation_score > 0.8`

---

## Internship Project: Machine Learning–Based Cyber Attack Behavior Prediction System

During my **Blue Team internship**, I used this dataset to build a **real-time Cyber Attack Behavior Prediction System**, which:

1. **Monitored network and user behavior** for suspicious activity.
2. **Predicted attacks before they occur** using supervised ML models.
3. **Integrated feature importance and thresholds** for alerts in the SOC environment.
4. **Generated insights and reports** for actionable security decisions.

**Technologies Used:** Python, Scikit-learn, Pandas, Matplotlib, Tkinter GUI (for visual dashboards), Random Forest, XGBoost, LSTM.

**Impact:**

* Detected brute-force login attempts, unusual session durations, and suspicious IP activity.
* Helped the SOC team prevent potential intrusions in real time.
* Provided a framework for combining supervised, unsupervised, and rule-based detection approaches.

---

## Challenges & Considerations

* **Adversarial Attacks:** Attackers may manipulate traffic to evade detection.
* **Concept Drift:** Cyber threats evolve, requiring continuous model updates.
* **False Positives & False Negatives:** Balancing detection sensitivity to avoid unnecessary alerts.

---

## Dataset Summary

* **Total records:** 9,537
* **Total features:** 10
* **File:** `cybersecurity_intrusion_data.csv` (~725 KB)
* **License:** MIT

**Feature Distribution Examples:**

* `network_packet_size`: Most packets between 430–552 bytes (~2,290 sessions)
* `protocol_type`: TCP 69%, UDP 25%, Other 5%
* `encryption_used`: AES 49%, DES 30%, Other 21%
* `login_attempts`: Mostly 1–3 attempts per session
* `ip_reputation_score`: 0–1 scale indicating suspicious activity

---


