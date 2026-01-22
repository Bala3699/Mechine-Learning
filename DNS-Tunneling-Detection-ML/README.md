# 🔐 DNS Tunneling Detection Using Machine Learning

## 📌 Overview

DNS tunneling is a stealthy attack technique used by malware and attackers to exfiltrate data and maintain command-and-control (C2) communication by embedding malicious payloads inside DNS queries and responses.

This project applies **Machine Learning algorithms** to detect **malicious DNS tunneling traffic** using real-world network flow data from the **CIC dataset - 2018**.

---

## 🎯 Project Objectives

* Detect covert DNS-based data exfiltration
* Classify benign and malicious DNS traffic
* Apply supervised and unsupervised ML algorithms
* Assist network security and threat-hunting teams

---

## 🧠 Machine Learning Algorithms Used

* **Random Forest Classifier**
* **Support Vector Machine (SVM)**
* **K-Means Clustering (Unsupervised Anomaly Detection)**

---

## 📂 Dataset Information

* **Dataset Name:** CIC Network Traffic Dataset
* **File:** `cic.csv`
* **Total Records:** 1,048,575
* **Features:** 80 network flow features
* **Labels:** Benign and multiple attack classes

---

## Structure (DNS-Tunneling)
```
DNS-Tunneling-Detection-ML/
│
├── README.md
├── dns_tunneling_ml.py
├── cic.csv
├── requirements.txt
└── results/
```
---

## 🛠️ Tools & Technologies

* **Language:** Python
* **Libraries:**

  * Pandas
  * NumPy
  * Scikit-learn
  * Matplotlib

---

## ⚙️ Methodology

1. Load and explore DNS traffic dataset
2. Preprocess data (cleaning, encoding, scaling)
3. Train supervised ML models (RF, SVM)
4. Apply K-Means for anomaly detection
5. Evaluate models using accuracy and classification metrics
6. Visualize performance comparison

---

## 📊 Results & Performance

| Model         | Accuracy                          |
| ------------- | --------------------------------- |
| Random Forest | **99.99%**                        |
| SVM           | **99.99%**                        |
| K-Means       | Unsupervised (Anomaly Clustering) |

✔ Random Forest achieved the best performance due to its ability to handle high-dimensional network traffic data.

---

## 📈 Sample Output

```
Random Forest Accuracy: 0.99997
SVM Accuracy: 0.99993
```

---

## 🔍 Key Findings

* DNS tunneling attacks exhibit unique traffic patterns
* ML models effectively detect hidden malicious activity
* Unsupervised clustering helps identify unknown threats

---

## 🚀 How to Run the Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Program

```bash
python dns_tunneling_ml.py
```

---

## 📌 Use Cases

* Network intrusion detection
* Malware C2 communication detection
* SOC threat hunting
* Academic and cybersecurity research

---

## 👨‍💻 Author

**Balamurugan**
Cybersecurity | Ethical Hacking | Machine Learning

---

## ⚠️ Disclaimer

This project is for **educational and research purposes only**.
