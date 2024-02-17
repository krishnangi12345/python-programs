def count_occurrences(lst, element):
    return lst.count(element)

my_list = [1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 1]
element = int(input("Enter the element to count occurrences: "))
print("Number of occurrences of", element, "in the list:", count_occurrences(my_list, element))
