# logistic_model.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv(os.path.join(path, "cybersecurity_attacks.csv"))
print("Dataset Shape:", df.shape)
print(df.head())
df.dropna(inplace=True)
label_cols = [
    'Protocol', 'Packet Type', 'Traffic Type',
    'Attack Type', 'Severity Level'
]

encoder = LabelEncoder()
for col in label_cols:
    df[col] = encoder.fit_transform(df[col])


df['Attack_Label'] = np.where(df['Attack Type'] > 0, 1, 0)

X = df[[
    'Source Port', 'Destination Port',
    'Packet Length', 'Anomaly Scores',
    'Protocol', 'Traffic Type'
]]

y = df['Attack_Label']


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


model = LogisticRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]  


accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", accuracy)

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))


cm = confusion_matrix(y_test, y_pred)

sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()


threshold = 0.5
custom_pred = (y_prob >= threshold).astype(int)

print("\nThreshold-based Accuracy:",
      accuracy_score(y_test, custom_pred))
