def fibonacci(n):
    if n == 0:
        return None

    elif n == 1:
        return 0

    elif n < 0:
        return "This is not possible!!."

    else:
        series = [0, 1]
        for start in range(n - 2):
            series.append(series[-1] + series[-2])
        for element in series:
            print(element)


number = int(input("Enter a number: "))
fibonacci(number)
