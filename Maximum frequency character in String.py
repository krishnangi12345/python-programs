from collections import Counter

def maximum_frequency_character(string):
    frequency = Counter(string)
    return max(frequency, key=frequency.get)

string = input("Enter a string: ")
print("Maximum frequency character:", maximum_frequency_character(string))
