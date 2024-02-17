def find_largest(lst):
    return max(lst)

my_list = [int(x) for x in input("Enter elements of the list separated by space: ").split()]
print("Largest number in the list:", find_largest(my_list))
