# LOAD DATASET FROM KAGGLEHUB

import os
import kagglehub
import pandas as pd

path = kagglehub.dataset_download(
    "dnkumars/cybersecurity-intrusion-detection-dataset"
)

print("Dataset folder:", path)
print("Files inside:", os.listdir(path))

csv_path = os.path.join(path, "cybersecurity_intrusion_data.csv")
df = pd.read_csv(csv_path)

print(df.head())
print(df.shape)
print(df.info())
print(df['attack_detected'].value_counts())

# DATA CLEANING

# Replace infinite values
df.replace([float('inf'), -float('inf')], pd.NA, inplace=True)

# Fill missing categorical values safely
df['encryption_used'] = df['encryption_used'].fillna('Unknown')

# Drop remaining missing rows
df.dropna(inplace=True)

# FEATURE / TARGET SEPARATION
y = df['attack_detected']

# Drop ID & target column from features
X = df.drop(columns=['session_id', 'attack_detected'])


# TRAIN TEST SPLIT

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

# ================================
# ENCODE CATEGORICAL FEATURES
# ================================

categorical_cols = X_train.select_dtypes(include='object').columns

X_train_enc = pd.get_dummies(X_train, columns=categorical_cols, drop_first=True)
X_test_enc = pd.get_dummies(X_test, columns=categorical_cols, drop_first=True)

# Align train & test columns
X_train_enc, X_test_enc = X_train_enc.align(
    X_test_enc,
    join='left',
    axis=1,
    fill_value=0
)

# ================================
# FEATURE SCALING
# ================================
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_enc)
X_test_scaled = scaler.transform(X_test_enc)

# ================================
# TRAIN MODEL
# ================================
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# ================================
# EVALUATION
# ================================
from sklearn.metrics import classification_report, confusion_matrix

y_pred = model.predict(X_test_scaled)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ================================
# PLOT CLASS DISTRIBUTION
# ================================
import matplotlib.pyplot as plt

counts = y.value_counts().sort_index()

plt.figure(figsize=(6, 4))
plt.bar(['Benign', 'Attack'], counts.values)
plt.title("Attack vs Benign Traffic Distribution")
plt.xlabel("Traffic Type")
plt.ylabel("Number of Records")
plt.tight_layout()
plt.show()

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=200,
    class_weight='balanced',
    random_state=42
)
model.fit(X_train_enc, y_train)

# ================================
# EVALUATE RANDOM FOREST
# ================================
y_pred_rf = model.predict(X_test_enc)

print("\nRandom Forest Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_rf))

print("\nRandom Forest Classification Report:")
print(classification_report(y_test, y_pred_rf))




