def is_perfect_square(x):
    s = int(x**0.5)
    return s*s == x

def is_fibonacci(num):
    return is_perfect_square(5*num*num + 4) or is_perfect_square(5*num*num - 4)

number = int(input("Enter a number: "))

if is_fibonacci(number):
    print(number, "is a Fibonacci number")
else:
    print(number, "is not a Fibonacci number")
