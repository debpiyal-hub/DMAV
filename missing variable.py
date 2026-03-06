import pandas as pd

# Sample dataset with missing values
data = {
    "Name": ["Alice", "Bob", None, "David"],
    "Age": [25, None, 30, 22],
    "Salary": [50000, 60000, None, 52000]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# 1. Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# 2. Drop rows with missing values
df_dropped = df.dropna()
print("\nData after dropping rows with missing values:")
print(df_dropped)

# 3. Fill missing values
df_filled = df.fillna({
    "Name": "Unknown",
    "Age": df["Age"].mean(),
    "Salary": df["Salary"].median()
})

print("\nData after filling missing values:")
print(df_filled)

# 4. Forward fill method
df_forward = df.fillna(method="ffill")
print("\nForward filled data:")
print(df_forward)