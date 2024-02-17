def n_largest_elements(lst, n):
    if len(lst) < n:
        return "List has less than", n, "elements"
    return sorted(lst, reverse=True)[:n]

my_list = [int(x) for x in input("Enter elements of the list separated by space: ").split()]
n = int(input("Enter the value of N: "))
print("N largest elements in the list:", n_largest_elements(my_list, n))
