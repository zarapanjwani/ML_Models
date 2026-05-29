# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
file = pd.read_csv("WindPower.csv")

# Store columns in variables
x = file["Wind speed (m/s)"]
y = file["Power (kW)"]

# -----------------------------
# Scatter Plot
# -----------------------------
plt.figure(figsize=(8,5))
plt.scatter(x, y)
plt.title("Wind Speed vs Power")
plt.xlabel("Wind Speed (m/s)")
plt.ylabel("Power (kW)")
plt.grid(True)
plt.show()

# -----------------------------
# Histogram
# -----------------------------
plt.figure(figsize=(8,5))
plt.hist(y, bins=20)
plt.title("Power Distribution")
plt.xlabel("Power (kW)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# -----------------------------
# Line Graph
# -----------------------------
plt.figure(figsize=(8,5))
plt.plot(x, y)
plt.title("Line Graph of Wind Speed and Power")
plt.xlabel("Wind Speed (m/s)")
plt.ylabel("Power (kW)")
plt.grid(True)
plt.show()