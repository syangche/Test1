def reverse_string(s):
    # Base case: If the string is empty or has only one character, return it
    if len(s) <= 1:
        return s

    # Recursive case:
    # 1. Get the first character of the string
    first_char = s[0]

    # 2. Get the remaining characters (excluding the first character)
    remaining_chars = s[1:]

    # 3. Recursively reverse the remaining characters
    reversed_remaining = reverse_string(remaining_chars)

    # 4. Append the first character to the end of the reversed remaining characters
    reversed_string = reversed_remaining + first_char

    return reversed_string

print(reverse_string("hello"))

