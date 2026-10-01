import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [100, 150, 120, 180, 200, 250]

plt.plot(months, sales, marker="o")

plt.title("Monthly Sales Dashboard")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)

plt.savefig("sales_chart.png")
plt.show()
