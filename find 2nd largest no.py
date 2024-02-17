def second_largest(lst):
    if len(lst) < 2:
        return "List has less than two elements"
    largest = max(lst[0], lst[1])
    second_largest = min(lst[0], lst[1])
    for i in range(2, len(lst)):
        if lst[i] > largest:
            second_largest = largest
            largest = lst[i]
        elif lst[i] > second_largest and lst[i] != largest:
            second_largest = lst[i]
    return second_largest

my_list = [int(x) for x in input("Enter elements of the list separated by space: ").split()]
print("Second largest number in the list:", second_largest(my_list))
