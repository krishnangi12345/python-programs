def remove_elements(lst, indices):
    indices.sort(reverse=True)
    for i in indices:
        del lst[i]
    return lst

my_list = [int(x) for x in input("Enter elements of the list separated by space: ").split()]
indices = [int(x) for x in input("Enter indices of elements to remove separated by space: ").split()]
print("List after removing elements:", remove_elements(my_list, indices))
