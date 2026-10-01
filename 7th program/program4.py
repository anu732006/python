import pandas as pd
import numpy as np

data = {
    "Product": ["Laptop", "Mobile", "Laptop", "Mobile", "Tablet"],
    "Quantity": [2, 5, 3, 4, 6],
    "Price": [50000, 20000, 50000, 20000, 15000]
}

df = pd.DataFrame(data)

# Calculate sales
df["Sales"] = np.array(df["Quantity"]) * np.array(df["Price"])

print("SALES DATA")
print(df)

# Product-wise analysis
result = df.groupby("Product")["Sales"].sum()

print("\nPRODUCT-WISE SALES")
print(result)

print("\nTotal Sales:", df["Sales"].sum())