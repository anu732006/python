import pandas as pd
import numpy as np

data = {
    "Month": ["January", "February", "March", "April", "May"],
    "Sales": [50000, 65000, 70000, 55000, 80000]
}

df = pd.DataFrame(data)

sales = np.array(df["Sales"])

print("MONTHLY SALES")
print(df)

print("\nTotal Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))
print("Maximum Sales:", np.max(sales))
print("Minimum Sales:", np.min(sales))