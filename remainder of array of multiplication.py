def array_remainder(arr, n):
    result = 1
    for num in arr:
        result = (result * num) % n
    return result

arr = [int(x) for x in input("Enter elements of the array separated by space: ").split()]
n = int(input("Enter the value of n: "))
print("Reminder of array multiplication divided by n:", array_remainder(arr, n))
