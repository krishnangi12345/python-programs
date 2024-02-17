import random
import string

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def generate_until_match(target_string):
    length = len(target_string)
    generated_string = ""
    while generated_string != target_string:
        generated_string = generate_random_string(length)
        print(generated_string)

# Example usage:
target = "hello"
generate_until_match(target)
