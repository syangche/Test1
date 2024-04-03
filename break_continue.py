outer_loop = True
while outer_loop:
  for number in range(1, 9):
    if number == 3:
      print(f"Skipping {number} in the inner loop")
      continue  # Skip number 3 in the inner loop
    if number == 7:
      print(f"Reached {number}, breaking outer loop")
      outer_loop = False  # Break out of the outer loop
      break  # Exit the inner loop (optional)
    else:
      print(number)