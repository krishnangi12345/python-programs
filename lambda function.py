def sort_list_of_dicts_by_value_using_lambda(list_of_dicts, key):
    return sorted(list_of_dicts, key=lambda x: x[key])

# Example usage:
my_list = [{'name': 'John', 'age': 25}, {'name': 'Alice', 'age': 20}, {'name': 'Bob', 'age': 30}]
sorted_list = sort_list_of_dicts_by_value_using_lambda(my_list, 'age')
print("Sorted list by age:", sorted_list)
