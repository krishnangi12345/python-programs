def find_smallest(lst):
    return min(lst)

my_list = [int(x) for x in input("Enter elements of the list separated by space: ").split()]
print("Smallest number in the list:", find_smallest(my_list))
