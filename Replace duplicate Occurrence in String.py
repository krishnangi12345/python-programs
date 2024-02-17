def replace_duplicate_occurrence(string):
    seen = set()
    result = []
    for char in string:
        if char in seen:
            result.append('$')  # or any other replacement character
        else:
            result.append(char)
            seen.add(char)
    return ''.join(result)

# Example usage:
input_string = "hello"
result = replace_duplicate_occurrence(input_string)
print("String with duplicate occurrences replaced:", result)

