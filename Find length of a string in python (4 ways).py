# Method 1: Using len() function
string = input("Enter a string: ")
print("Length of the string:", len(string))

# Method 2: Using loop
count = 0
for char in string:
    count += 1
print("Length of the string:", count)

# Method 3: Using string's __len__() method
print("Length of the string:", string.__len__())

# Method 4: Using list comprehension
print("Length of the string:", sum(1 for _ in string))
