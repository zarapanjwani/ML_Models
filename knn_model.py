# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error

# Load dataset
file = pd.read_csv("WindPower.csv")

# Input and output
X = file[["Wind speed (m/s)"]]
y = file["Power (kW)"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create KNN model
model = KNeighborsRegressor(n_neighbors=5)

# Train model
model.fit(X_train, y_train)

# Predict values
predictions = model.predict(X_test)

# Calculate MAE
mae = mean_absolute_error(y_test, predictions)

print("Mean Absolute Error:")
print(mae)

# Predict new value
new_speed = [[10]]
new_prediction = model.predict(new_speed)

print("\nPredicted Power for Wind Speed 10 m/s:")
print(new_prediction)