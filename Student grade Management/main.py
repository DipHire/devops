import grades
import validation
import reports

name = input("Enter the Student Name:=>  ")

if not validation.validate_name(name):
    print("Enter Valid Name")
    exit()

marks = []
subjects = int(input("Enter number of subjects:=>  "))

for i in range(subjects):
    m = int(input(f"Enter marks for subject {i+1}:=> "))
    marks.append(m)

if not validation.validate_marks(marks):
    print("Invalid marks entered!(Marks should be in range of 0-100)")
    exit()

total = grades.calculate_total(marks)
percentage = grades.calculate_percentage(total, subjects * 100)
grade = grades.calculate_grade(percentage)

reports.generate_report(name, marks, total, percentage, grade)
