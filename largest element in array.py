def find_largest(arr):
    return max(arr)

arr = [int(x) for x in input("Enter elements of the array separated by space: ").split()]
print("Largest element in the array:", find_largest(arr))
