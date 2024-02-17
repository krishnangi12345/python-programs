def print_even_length_words(s):
    return [word for word in s.split() if len(word) % 2 == 0]

string = input("Enter a string: ")
print("Even length words in the string:", print_even_length_words(string))
