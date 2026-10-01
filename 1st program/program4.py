# Find Student with Lowest Marks

n = int(input("Enter number of students: "))

lowest = 101
low_student = ""

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    if marks < lowest:
        lowest = marks
        low_student = name

print("Lowest Mark Student:", low_student)
print("Lowest Marks:", lowest)