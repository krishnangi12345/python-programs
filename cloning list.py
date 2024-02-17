# Method 1: Using the slice operator
original_list = [1, 2, 3, 4, 5]
cloned_list = original_list[:]
print("Cloned list:", cloned_list)

# Method 2: Using the list() constructor
original_list = [1, 2, 3, 4, 5]
cloned_list = list(original_list)
print("Cloned list:", cloned_list)

# Method 3: Using the copy() method
original_list = [1, 2, 3, 4, 5]
cloned_list = original_list.copy()
print("Cloned list:", cloned_list)
