def count_matching_characters(string1, string2):
    return sum(1 for char1, char2 in zip(string1, string2) if char1 == char2)

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
print("Number of matching characters:", count_matching_characters(string1, string2))
