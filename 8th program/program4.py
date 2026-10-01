import matplotlib.pyplot as plt

# Student data
students = ["Anu", "Bala", "Cathy", "David", "Esha"]
marks = [78, 85, 72, 90, 88]

# Subject data
subjects = ["Python", "Java", "DBMS", "Web"]
average = [82, 75, 80, 88]

# Create figure with two charts
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# -------------------------
# Bar Chart - Student Marks
# -------------------------
ax[0].bar(students, marks, color="skyblue")

ax[0].set_title("Student Marks")
ax[0].set_xlabel("Students")
ax[0].set_ylabel("Marks")
ax[0].set_ylim(0, 100)

# Show marks on top of bars
for i, mark in enumerate(marks):
    ax[0].text(i, mark + 2, str(mark), ha="center")

# -------------------------
# Line Chart - Subject Average
# -------------------------
ax[1].plot(
    subjects,
    average,
    marker="o",
    color="green",
    linewidth=2
)

ax[1].set_title("Subject Average")
ax[1].set_xlabel("Subject")
ax[1].set_ylabel("Average Marks")
ax[1].set_ylim(0, 100)
ax[1].grid(True)

# Show values on points
for i, value in enumerate(average):
    ax[1].text(i, value + 2, str(value), ha="center")

# Adjust layout
plt.tight_layout()

# Save chart
plt.savefig("student_marks.png", dpi=150)

# Display chart
plt.show()
