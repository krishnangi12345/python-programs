def check_element(lst, element):
    return element in lst

my_list = [int(x) for x in input("Enter elements of the list separated by space: ").split()]
element = int(input("Enter the element to check: "))
if check_element(my_list, element):
    print("Element", element, "exists in the list.")
else:
    print("Element", element, "does not exist in the list.")
