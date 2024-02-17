def find_long_words(sentence, k):
    words = sentence.split()
    long_words = [word for word in words if len(word) > k]
    return long_words

# Example usage:
sentence = "This is a sample sentence with some long words"
k = 4
result = find_long_words(sentence, k)
print("Words longer than", k, "characters:", result)
