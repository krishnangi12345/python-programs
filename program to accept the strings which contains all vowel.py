def contains_all_vowels(s):
    vowels = set('aeiouAEIOU')
    return vowels.issubset(set(s))

string = input("Enter a string: ")
if contains_all_vowels(string):
    print("The string contains all vowels.")
else:
    print("The string does not contain all vowels.")
