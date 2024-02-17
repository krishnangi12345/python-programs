def remove_duplicates(string):
    return ''.join(char for char in string if string.count(char) == 1)

string = input("Enter a string: ")
print("String after removing duplicates:", remove_duplicates(string))
