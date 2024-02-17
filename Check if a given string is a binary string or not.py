def is_binary_string(s):
    for char in s:
        if char != '0' and char != '1':
            return False
    return True

# Example usage:
input_string = "1010101"
if is_binary_string(input_string):
    print("The given string is a binary string.")
else:
    print("The given string is not a binary string.")
