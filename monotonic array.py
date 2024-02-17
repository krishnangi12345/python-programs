def is_monotonic(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) or all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))

arr = [int(x) for x in input("Enter elements of the array separated by space: ").split()]
if is_monotonic(arr):
    print("The given array is monotonic.")
else:
    print("The given array is not monotonic.")
