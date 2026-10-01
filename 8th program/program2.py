import matplotlib.pyplot as plt

departments = ["CS", "AI", "BCA", "BSC"]
students = [80, 65, 75, 55]

plt.bar(departments, students)

plt.title("Department-wise Student Count")
plt.xlabel("Department")
plt.ylabel("Number of Students")

plt.savefig("department_students.png")
plt.show()
