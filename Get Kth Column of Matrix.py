def get_kth_column(matrix, k):
    return [row[k-1] for row in matrix]

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
k = int(input("Enter the column number (K): "))
print("Kth column of the matrix:")
print(get_kth_column(matrix, k))
