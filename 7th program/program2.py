import pandas as pd
import numpy as np

data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Printer"],
    "Sales": [100000, 150000, 75000, 50000]
}

df = pd.DataFrame(data)

print("SALES DATA")
print(df)

# Find highest sale
highest = df["Sales"].max()

product = df.loc[df["Sales"].idxmax(), "Product"]

print("\nHighest Sales:", highest)
print("Product:", product)