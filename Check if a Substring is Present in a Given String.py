def is_substring_present(s, sub):
    return sub in s

string = input("Enter a string: ")
substring = input("Enter a substring to check: ")
if is_substring_present(string, substring):
    print("The substring is present in the string.")
else:
    print("The substring is not present in the string.")
