def split_and_join(s):
    words = s.split()
    joined_string = "-".join(words)
    return joined_string

# Example usage:
s = "This is a sample string"
result = split_and_join(s)
print("String after split and join:", result)
