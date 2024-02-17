def print_even_numbers(start, end):
    return [num for num in range(start, end+1) if num % 2 == 0]

start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))
print("Even numbers in the range:", print_even_numbers(start, end))
