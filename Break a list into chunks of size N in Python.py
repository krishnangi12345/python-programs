def chunks(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk_size = int(input("Enter the size of each chunk: "))
print("List after breaking into chunks:", chunks(my_list, chunk_size))
