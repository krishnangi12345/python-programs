def cube_sum(n):
    return (n * (n + 1) // 2) ** 2

n = int(input("Enter the value of n: "))
print("Cube sum of first", n, "natural numbers is:", cube_sum(n))
