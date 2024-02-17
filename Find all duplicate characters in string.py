from collections import Counter

def find_duplicate_characters(string):
    counter = Counter(string)
    duplicates = [char for char, count in counter.items() if count > 1]
    return duplicates

# Example usage:
input_string = "hello"
result = find_duplicate_characters(input_string)
print("Duplicate characters:", result)
