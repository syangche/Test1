# Calculate total grade of each student and find overall average grade of the class
num_students = int(input("Enter the number of students: "))
total_class_grade = 0
for i in range(1, num_students + 1):
    total_grade = 0
    num_grades = int(input(f"Enter the number of grades for student {i}: "))
    for j in range(1, num_grades + 1):
        grade = float(input(f"Enter grade {j} for student {i}: "))
        total_grade += grade
    average_grade = total_grade / num_grades
    total_class_grade += total_grade
    print(f"Total grade for student {i}: {total_grade:.2f}")
overall_average_grade = total_class_grade / (num_students * num_grades)
print(f"Overall average grade of the class: {overall_average_grade:.2f}")
