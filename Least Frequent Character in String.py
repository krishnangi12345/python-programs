from collections import Counter

def least_frequent_character(string):
    frequency = Counter(string)
    return min(frequency, key=frequency.get)

string = input("Enter a string: ")
print("Least frequent character:", least_frequent_character(string))
