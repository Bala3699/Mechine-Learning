# 🎬 Machine Learning–Based Cyber Attack Behavior Prediction System

## Introduction
In the modern digital era, cybersecurity threats are constantly evolving. Organizations face challenges from attacks like DDoS, phishing, ransomware, SQL injection, and malware. This project presents a **Machine Learning–Based Cyber Attack Behavior Prediction System**, designed to analyze network traffic and predict potential cyber attacks in real time.

This documentary covers the system's **purpose, design, methodology, user interface, machine learning models, and results**.

---

## 🎯 Objective
The primary goals of this project are:

- Detect and classify various types of cyber attacks.
- Provide a user-friendly interface for system monitoring.
- Visualize attack patterns and prediction results.
- Offer actionable insights for cybersecurity teams.

---

## 📁 Dataset
The system uses a curated **network intrusion dataset** containing labeled samples for multiple attack types:

| Attack Type       | Description                                      |
|------------------|--------------------------------------------------|
| DDoS              | Distributed Denial-of-Service attacks           |
| Phishing          | Fraudulent attempts to steal sensitive data     |
| SQL Injection     | Database manipulation attacks                    |
| Ransomware        | Malware that encrypts files for ransom          |
| Malware           | Malicious software causing system compromise   |

> Dataset provides **network traffic features, user behavior logs, and attack labels**. It is preprocessed to handle missing values and normalize features before model training.

---

## 🧠 Machine Learning Models

The project uses supervised machine learning algorithms to classify cyber attacks:

| Algorithm           | Description                                               |
|--------------------|-----------------------------------------------------------|
| Random Forest       | Ensemble learning method, robust against overfitting     |
| Decision Tree       | Simple interpretable model                                |
| Logistic Regression | Baseline linear classifier for binary/multi-class        |
| Support Vector Machine (SVM) | Separates classes with a hyperplane in feature space |

**Pipeline Overview:**
1. Data preprocessing (encoding, normalization)
2. Feature selection
3. Model training and evaluation
4. Prediction and visualization

---

## 🖥️ GUI Overview

The system includes a **Tkinter-based GUI** for interaction:

- **Login & Authentication**  
  Secure login with master key and optional OTP verification.

- **Attack Prediction Dashboard**  
  Upload network traffic CSV files to predict attack type.  
  Results are visualized using **bar charts and highlighted tables**.

- **Real-time Monitoring**  
  - File activity monitoring  
  - Process monitoring (CPU, RAM, unknown processes)  
  - Network sniffing for suspicious traffic  

- **Encryption & Steganography Module**  
  Secure sensitive logs using combined encryption and zero-width steganography.

- **Password Management**  
  Forgot Password feature via **QR-based OTP**.

**Screenshot Placeholder:**

![assest](https://github.com/Bala3699/Mechine-Learning/blob/main/Cyber%20Attack%20Behavior%20Prediction%20System/assest/Screenshot%202026-01-30%20142741.png)
![assest](https://github.com/Bala3699/Mechine-Learning/blob/main/Cyber%20Attack%20Behavior%20Prediction%20System/assest/Screenshot%202026-01-28%20221849.png)
![assest](https://github.com/Bala3699/Mechine-Learning/blob/main/Cyber%20Attack%20Behavior%20Prediction%20System/assest/Screenshot%202026-01-30%20142809.png)



---

## 📊 Visualization
The system generates **dynamic plots** to visualize attack data:

- Bar chart of attack counts
- Highlighted rows for detected attacks
- Real-time updates during monitoring

```python
# Example plot snippet
import matplotlib.pyplot as plt

attacks = ['DDoS', 'Phishing', 'Ransomware', 'SQL Injection', 'Malware']
counts = [120, 45, 30, 20, 75]

plt.bar(attacks, counts, color='red')
plt.title("Detected Cyber Attacks")
plt.show()
````

> Each detected attack is highlighted in the GUI for easy recognition.

---

## 🔧 Features Summary

* **Multi-attack detection**: DDoS, Phishing, SQL Injection, Ransomware, Malware
* **Machine learning-based prediction**
* **Interactive and user-friendly GUI**
* **Real-time system monitoring**
* **File & network security via encryption and steganography**
* **Forgot Password with QR-based OTP**
* **Export logs for reporting and auditing**

---

## ⚙️ System Architecture

```
[Network Traffic CSV] --> [Preprocessing] --> [ML Model] --> [Prediction]
                                              |
                                              v
                                     [GUI Dashboard & Visualization]
```

* **Preprocessing**: Handles missing values, label encoding, feature scaling.
* **ML Model**: Random Forest for multi-class classification.
* **GUI Dashboard**: Real-time visualization and monitoring.

---

## 📈 Results

The system is able to:

* Classify attacks with **high accuracy** (≈ 90%+ with Random Forest)
* Highlight suspicious activity in **real time**
* Provide detailed logs for each prediction
* Show trends and patterns of attacks

**Example Output Table:**

| Timestamp        | Source IP   | Attack Type | Confidence |
| ---------------- | ----------- | ----------- | ---------- |
| 2026-01-30 12:00 | 192.168.1.5 | DDoS        | 0.92       |
| 2026-01-30 12:01 | 10.0.0.15   | Phishing    | 0.87       |

---

## 💡 Future Work

* Integration with **SIEM tools** for enterprise-level monitoring
* Deploy the system as a **web-based dashboard**
* Include **unsupervised learning** for zero-day attack detection
* Extend real-time monitoring to **entire network traffic**

---

## 📝 Conclusion

The **Machine Learning–Based Cyber Attack Behavior Prediction System** demonstrates how machine learning can enhance cybersecurity efforts. By combining predictive modeling, interactive GUI, and real-time monitoring, the system provides a comprehensive solution for **blue team analysts** and cybersecurity professionals.

> This project can serve as a foundation for more advanced **SOC automation** and **threat intelligence pipelines**.

---

## 📂 Repository Structure

```
CyberAttackPrediction/
├── cyber_attack_model.pkl        # Trained ML model
├── main.py                       # GUI & main application
├── requirements.txt              # Python dependencies
├── assets/
│   └── gui_screenshot.png        # GUI screenshot
└── datasets/
    └── network_attacks.csv       # Sample dataset
```

