recursive_sum = lambda n: 1 if n == 1 else n + recursive_sum(n - 1)
factorial = lambda n: 1 if n == 0 or n == 1 else n * factorial(n - 1)
multiply = lambda a, b: a * b
greater = lambda a, b: a if a > b else b
print("Choose an operation:")
print("1. Sum of numbers from 1 to n")
print("2. Factorial of n")
print("3. Multiplication of two numbers")
print("4. Find greater between two numbers")
choice = int(input("Enter your choice (1-4): "))
if choice in [1, 2]:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Enter a positive value")
    else:
        result = recursive_sum(num) if choice == 1 else factorial(num)
        print(result)
elif choice in [3, 4]:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = multiply(a, b) if choice == 3 else greater(a, b)
    print(result)
else:
    print("Invalid choice!")