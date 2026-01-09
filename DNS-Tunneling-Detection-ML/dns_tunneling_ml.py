import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# =========================
# 1. Load Dataset
# =========================
df = pd.read_csv(f"{path}/cic.csv")

# Standardize column names by stripping whitespace and converting to lowercase
df.columns = df.columns.str.strip().str.lower()

print("Dataset Shape:", df.shape)
print(df.head())

# =========================
# 2. Data Preprocessing
# =========================

# Drop non-numeric or irrelevant columns if present
for col in df.columns:
    if df[col].dtype == 'object':
        if col != 'label': # 'label' should now be lowercase and stripped
            df.drop(col, axis=1, inplace=True)

# Encode labels
if 'label' in df.columns:
    le = LabelEncoder()
    df['label'] = le.fit_transform(df['label'])

# Handle missing values and infinite values only for numeric columns
numeric_cols = df.select_dtypes(include=np.number).columns

# Replace infinite values with NaN
df[numeric_cols] = df[numeric_cols].replace([np.inf, -np.inf], np.nan)

# Now fill NaN values with the mean (which will include formerly infinite values)
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# =========================
# 3. Feature & Target Split
# =========================
X = df.drop('label', axis=1)
y = df['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# =========================
# 4. Random Forest Model
# =========================
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)

print("\n--- Random Forest Results ---")
print("Accuracy:", accuracy_score(y_test, rf_pred))
print(classification_report(y_test, rf_pred))

# =========================
# 5. Support Vector Machine
# =========================
svm = SVC(kernel='rbf')
svm.fit(X_train, y_train)
svm_pred = svm.predict(X_test)

print("\n--- SVM Results ---")
print("Accuracy:", accuracy_score(y_test, svm_pred))
print(classification_report(y_test, svm_pred))

# =========================
# 6. K-Means Clustering
# =========================
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X_train)
kmeans_pred = kmeans.predict(X_test)

print("\n--- K-Means Results (Unsupervised) ---")
print("Confusion Matrix:")
print(confusion_matrix(y_test, kmeans_pred))

# =========================
# 7. Visualization
# =========================
plt.figure()
plt.bar(['Random Forest', 'SVM'],
        [accuracy_score(y_test, rf_pred), accuracy_score(y_test, svm_pred)])
plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy")
plt.show()
