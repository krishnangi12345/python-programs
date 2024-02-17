import re

def contains_url(s):
    pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    return bool(re.search(pattern, s))

# Example usage:
input_string = "This is a sample string with a URL https://example.com"
if contains_url(input_string):
    print("The string contains a URL.")
else:
    print("The string does not contain a URL.")
