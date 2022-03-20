def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

user = int(input("Enter a number to find its factorial: "))
print("The factorial of " + str(user) + " is " + str(factorial(user)))
