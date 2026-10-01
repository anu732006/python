import pandas as pd
import numpy as np

# Create sales data
data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile"],
    "Quantity": [2, 5, 3, 4, 6],
    "Price": [50000, 20000, 15000, 50000, 20000]
}

df = pd.DataFrame(data)

# Calculate sales
df["Sales"] = np.array(df["Quantity"]) * np.array(df["Price"])

print("SALES DATA")
print(df)

print("\nTotal Sales:", df["Sales"].sum())