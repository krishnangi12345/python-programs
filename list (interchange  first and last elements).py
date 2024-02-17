def interchange_first_last(lst):
    if len(lst) < 2:
        return lst
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

my_list = [int(x) for x in input("Enter elements of the list separated by space: ").split()]
print("List after interchanging first and last elements:", interchange_first_last(my_list))
