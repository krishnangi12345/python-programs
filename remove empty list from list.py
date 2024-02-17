def remove_empty_lists(lst):
    return [sublist for sublist in lst if sublist]

my_list = [[], [1, 2, 3], [], [], [4, 5], [], [6, 7, 8]]
print("List after removing empty lists:", remove_empty_lists(my_list))
