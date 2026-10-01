import matplotlib.pyplot as plt

# Data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [100, 130, 120, 160, 180, 200]

products = ["Laptop", "Mobile", "Tablet", "Watch"]
quantity = [40, 70, 35, 50]

# Create figure
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# -------------------------
# Line Chart
# -------------------------
ax[0].plot(months, sales, marker="o", color="blue", linewidth=2)

ax[0].set_title("Monthly Sales")
ax[0].set_xlabel("Month")
ax[0].set_ylabel("Sales")
ax[0].grid(True)

# -------------------------
# Bar Chart
# -------------------------
ax[1].bar(products, quantity, color="skyblue")

ax[1].set_title("Product Quantity")
ax[1].set_xlabel("Product")
ax[1].set_ylabel("Quantity")

# Add values on top of bars
for i, value in enumerate(quantity):
    ax[1].text(i, value + 2, str(value), ha="center")

# Adjust layout
plt.tight_layout()

# Save the charts
plt.savefig("sales_charts.png", dpi=150)

# Display
plt.show()
