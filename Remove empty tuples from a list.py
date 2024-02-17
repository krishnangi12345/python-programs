def remove_empty_tuples(lst):
    return [tup for tup in lst if tup]

my_list = [(), (1, 2), (), (3, 4), (), (), (5, 6)]
print("List after removing empty tuples:", remove_empty_tuples(my_list))
