def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return n
    return n * factorial(n - 1)


number = int(input("Enter a number: "))

print(factorial(number))
