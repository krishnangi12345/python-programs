def cumulative_sum(lst):
    result = []
    total = 0
    for num in lst:
        total += num
        result.append(total)
    return result

my_list = [1, 2, 3, 4, 5]
print("Cumulative sum of the list:", cumulative_sum(my_list))
