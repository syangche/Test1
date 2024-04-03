# Student grades
student_grades = [
    [85, 92, 78],  # Student 1
    [76, 88, 91],  # Student 2
    [91, 72, 85],  # Student 3
    [67, 95, 82],  # Student 4
    [79, 81, 74]   # Student 5
]

num_students = len(student_grades)
num_subjects = len(student_grades[0])

subject_totals = [0] * num_subjects

# Calculate subject totals
for student in student_grades:
    for i in range(num_subjects):
        subject_totals[i] += student[i]

# Calculate subject averages
subject_averages = [total / num_students for total in subject_totals]

# Print subject averages
subjects = ["English", "Math", "Science"]
for i in range(num_subjects):
    print(f"Class Average for {subjects[i]}: {subject_averages[i]:.2f}")