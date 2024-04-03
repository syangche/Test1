def first_repeating_character(s):
    char_count = {}  # Dictionary to store character counts
    
    # Single pass to count characters
    for c in s:
        if c in char_count:
            # Found repeating character, print its memory address and return
            print(f"The memory address of the first repeating character '{c}' is:", end=" ")
            return id(c)
        else:
            char_count[c] = 1
    
    return None  # or any specific indicator if no repeating character is found

# Example usage
print(first_repeating_character("people"))