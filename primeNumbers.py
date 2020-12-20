def isPrime(num):
    factors = 0
    for element in range(1, num + 1):
        if num % element == 0:
            factors += 1

    if factors == 2:
        return True

    else:
        return False


def primeNumbers(n):
    primeList = []
    element = 0
    while len(primeList) != n:
        element += 1
        if isPrime(element):
            primeList.append(element)

    for element in primeList:
        print(element)
    print(len(primeList))


number = int(input("Enter a number: "))
primeNumbers(number)
