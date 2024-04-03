

# Generate a multiplication table based on user input
num = int(input("Enter the number for which you want the multiplication table: "))
limit = int(input("Enter the limit up to which you want the multiplication table generated: "))

print(f"Multiplication Table for {num}:")
multiplier = 1
while multiplier <= limit:
    print(f"{num} x {multiplier} = {num * multiplier}")
    multiplier += 1
