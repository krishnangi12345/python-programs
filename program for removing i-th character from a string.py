def remove_character(s, i):
    if i < 0 or i >= len(s):
        return "Index out of range"
    return s[:i] + s[i+1:]

# Example usage:
s = "Hello World"
i = 3
result = remove_character(s, i)
print("String after removing", i, "th character:", result)
