# Import required libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import os
data = pd.read_csv(os.path.join(path, "realtime_ddos_traffic_dataset.csv"))
le = LabelEncoder()
data["traffic_type"] = le.fit_transform(data["traffic_type"].map({
    "Normal": 0,
    "DDoS": 1
}))
df = pd.DataFrame(data)

# Normal == 0, DDoS == 1

X = data.drop("traffic_type", axis=1)
y = data["traffic_type"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4, stratify=y)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Displaying the output

print("Mean Squared Error (MSE):", mse)
print("Mean Absolute Error (MAE):", mae)
print("R² Score:", r2)
print(df.isnull().sum())

# visuvalization

plt.figure(figsize=(10, 8))
sns.scatterplot(x='packet_count_per_second', y='byte_count_per_second', hue='traffic_type', data=df, palette='viridis', alpha=0.7)
plt.title('DDoS Detection: Packet Count vs. Byte Count per Second')
plt.xlabel('Packet Count per Second')
plt.ylabel('Byte Count per Second')
plt.show()
