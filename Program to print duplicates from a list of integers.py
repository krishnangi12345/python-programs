def print_duplicates(lst):
    seen = set()
    duplicates = set()
    for num in lst:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

my_list = [1, 2, 3, 4, 1, 2, 5, 6, 3, 7, 8, 9, 1, 3]
print("Duplicates in the list:", print_duplicates(my_list))
