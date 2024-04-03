num_students = int(input("Enter the number of students: "))

i = 1
while i <= num_students:
    total_grade = 0
    num_subjects = int(input(f"Enter the number of subjects for student {i}: "))
    
    for j in range(1, num_subjects + 1):
        grade = float(input(f"Enter subject {j} grade for student {i}: "))
        total_grade += grade
        
    average_grade = total_grade / num_subjects
    print(f"Average grade for student {i}: {average_grade:.2f}")
    i += 1

# This code snippet demonstrates nested loops with the outer loop as a while loop
# and the inner loop as a for loop.
# It prompts the user to enter the number of students and their grades.
# It then calculates the average grade for each student and prints the result.

