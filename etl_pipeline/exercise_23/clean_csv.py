import pandas as pd

# Extract: Read CSV file
df = pd.read_csv("dirty_data.csv")

# Transform: Remove duplicate rows
df = df.drop_duplicates()

# Transform: Remove blank rows
df = df.dropna(how="all")

# Transform: Fill missing ages
df["age"] = df["age"].fillna(df["age"].mean())

# Transform: Standardize date formats
df["date"] = pd.to_datetime(df["date"], format="mixed", dayfirst=True, errors="coerce")

df["date"] = df["date"].dt.strftime("%Y-%m-%d")

# Load: Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("ETL cleaning completed successfully")
