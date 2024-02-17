def print_positive_numbers(lst):
    return [num for num in lst if num > 0]

my_list = [int(x) for x in input("Enter elements of the list separated by space: ").split()]
print("Positive numbers in the list:", print_positive_numbers(my_list))
