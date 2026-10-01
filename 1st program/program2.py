# Find student with highest marks

n = int(input("Enter number of students: "))

highest = -1
top_student = ""

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    if marks > highest:
        highest = marks
        top_student = name

print("\nHighest Mark Student:", top_student)
print("Highest Marks:", highest)