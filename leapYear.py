from datetime import datetime


def isLeap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True

    if year % 100 == 0 and year % 400 == 0:
        return True

    else:
        return False


def leapYear(n):
    now = datetime.now().year
    leapList = []
    while len(leapList) != n:
        if isLeap(now):
            leapList.append(now)
        now += 1

    for element in leapList:
        print(element)


num = int(input("Enter a number: "))
leapYear(num)
