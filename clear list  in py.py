# Method 1: Using clear() method
my_list = [int(x) for x in input("Enter elements of the list separated by space: ").split()]
my_list.clear()
print("List after clearing using clear():", my_list)

# Method 2: Assigning an empty list
my_list = [int(x) for x in input("Enter elements of the list separated by space: ").split()]
my_list = []
print("List after clearing by assigning an empty list:", my_list)

# Method 3: Using del statement
my_list = [int(x) for x in input("Enter elements of the list separated by space: ").split()]
del my_list[:]
print("List after clearing using del:", my_list)
