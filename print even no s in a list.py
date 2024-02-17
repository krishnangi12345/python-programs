def print_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

my_list = [int(x) for x in input("Enter elements of the list separated by space: ").split()]
print("Even numbers in the list:", print_even_numbers(my_list))
