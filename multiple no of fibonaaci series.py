def fibonacci_multiple(n, x):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b * x

n = int(input("Enter the value of n: "))
x = int(input("Enter the value of x: "))
print("The", n, "th multiple of", x, "in the Fibonacci series is:", fibonacci_multiple(n, x))
