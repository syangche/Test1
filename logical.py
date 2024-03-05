# # Example 1
# x = 5
# print(x > 3 and x < 10)  # True because both conditions are True

# # Example 2
# y = 12
# print(y > 10 and y % 5 == 0)  # False because the second condition is False

# # Example 1
# x = 5
# print(x < 3 or x > 10)  # False because both conditions are False

# # Example 2
# y = 12
# print(y < 10 or y % 2 == 0)  # True because the second condition is True

# # Example 1
# x = 5
# print(not(x > 3 and x < 10))  # False because the condition inside the not is True

# # Example 2
# y = 12
# print(not(y > 10 and y % 5 == 0))  # True because the condition inside the not is False

# Step 1: Ask the user to input their age
age = int(input("Enter your age: "))

# Step 2: Ask the user to input whether they are a student or not
is_student = input("Are you a student? (yes/no): ")

# Step 3: Determine if the student is eligible for a discount based on age and student status
if age <= 12 or (13 <= age <= 18 and is_student == 'yes'):
    print("You are eligible for a discount on the movie ticket.")
else:
    print("You are not eligible for a discount on the movie ticket.")
