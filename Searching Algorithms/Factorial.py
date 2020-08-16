def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter a number: "))
f = factorial(n)
print("Factorial of " + str(n) + " is " + str(f))