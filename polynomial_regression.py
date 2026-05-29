# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
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

# Convert data into polynomial features
poly = PolynomialFeatures(degree=3)

X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train_poly, y_train)

# Predictions
predictions = model.predict(X_test_poly)

plt.show()