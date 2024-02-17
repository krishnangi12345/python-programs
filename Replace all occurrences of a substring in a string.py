def replace_substring(string, old_substring, new_substring):
    return string.replace(old_substring, new_substring)

# Example usage:
input_string = "hello world hello"
old_substring = "hello"
new_substring = "hi"
result = replace_substring(input_string, old_substring, new_substring)
print("String after replacement:", result)
