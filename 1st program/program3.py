# Student Grade Analyzer

students = int(input("Enter number of students: "))

for i in range(students):
    marks = int(input("Enter marks: "))

    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 50:
        print("Grade: C")
    else:
        print("Grade: F")