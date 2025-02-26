def recursive_sum(n):
    if n == 1:
        return 1
    return n + recursive_sum(n - 1)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Choose an operation:")
print("1. Sum of numbers from 1 to n")
print("2. Factorial of n")

choice = int(input("Enter your choice (1 or 2): "))
num = int(input("Enter a number: "))

if num < 0:
    print("Enter a positive value")
else:
    if choice == 1:
        result = recursive_sum(num)
        print(f"Sum of numbers from 1 to {num}: {result}")
    elif choice == 2:
        result = factorial(num)
        print(f"Factorial of {num}: {result}")
    else:
        print("Invalid choice! Please enter 1 or 2.")
