def find_uncommon_words(string1, string2):
    words1 = set(string1.split())
    words2 = set(string2.split())
    uncommon_words = words1.symmetric_difference(words2)
    return uncommon_words

# Example usage:
string1 = "apple banana mango"
string2 = "banana mango orange"
result = find_uncommon_words(string1, string2)
print("Uncommon words:", result)
