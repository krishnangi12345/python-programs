from itertools import permutations

def permutation_of_string(string):
    perms = [''.join(p) for p in permutations(string)]
    return perms

# Example usage:
input_string = "abc"
result = permutation_of_string(input_string)
print("Permutations of the given string:", result)
