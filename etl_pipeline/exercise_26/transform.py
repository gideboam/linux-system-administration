import pandas as pd
from datetime import datetime

# Read the CSV file
df = pd.read_csv("temperatures.csv")

# Convert Celsius to Fahrenheit
df["temperature_f"] = (df["temperature_c"] * 9/5) + 32

# Add processing timestamp
df["processed_timestamp"] = datetime.now()

# Save transformed data
df.to_csv("transformed_temperatures.csv", index=False)

print("Transformation completed successfully.")
