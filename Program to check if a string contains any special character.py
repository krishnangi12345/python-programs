import string

def contains_special_character(string):
    special_characters = set(string.punctuation)
    return any(char in special_characters for char in string)

string = input("Enter a string: ")
if contains_special_character(string):
    print("The string contains special character(s).")
else:
    print("The string does not contain any special characters.")
