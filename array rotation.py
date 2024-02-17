def rotate_array(arr, d):
    return arr[d:] + arr[:d]

arr = [int(x) for x in input("Enter elements of the array separated by space: ").split()]
d = int(input("Enter the number of rotations: "))
print("Array after rotation:", rotate_array(arr, d))
