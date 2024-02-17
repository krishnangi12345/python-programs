def multiply_elements(lst):
    result = 1
    for num in lst:
        result *= num
    return result

my_list = [int(x) for x in input("Enter elements of the list separated by space: ").split()]
print("Product of elements in the list:", multiply_elements(my_list))
