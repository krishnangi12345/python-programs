def is_symmetrical(s):
    return s == s[::-1]

def is_palindrome(s):
    return is_symmetrical(s)

string = input("Enter a string: ")
if is_symmetrical(string):
    print("The string is symmetrical.")
    if is_palindrome(string):
        print("Additionally, the string is also a palindrome.")
else:
    print("The string is not symmetrical.")
