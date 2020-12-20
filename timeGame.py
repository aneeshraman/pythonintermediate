def timeInterval(startHour, startMinute, startSecond, endHour, endMinute, endSecond):
    hourInterval = endHour - startHour
    minuteInterval = endMinute - startMinute
    secondInterval = endSecond - startSecond
    hourInterval *= 3600
    minuteInterval *= 60
    secondInterval = secondInterval
    return "Total time interval is " + str(sum([secondInterval, minuteInterval, secondInterval]))


startHour, startMinute, startSecond = input("Enter start time: ").split(":")

startHour = int(startHour)
startMinute = int(startMinute)
startSecond = int(startSecond)

endHour, endMinute, endSecond = input("Enter end time: ").split(":")

endHour = int(endHour)
endMinute = int(endMinute)
endSecond = int(endSecond)

if startHour > 24 or endHour > 24:
    raise Exception("Wrong input, hour cannot be greater than 24")

if startMinute > 60 or endMinute > 60:
    raise Exception("Wrong input, minute cannot be greater than 60")

if startSecond > 60 or endSecond > 60:
    raise Exception("Wrong input, second cannot be greater than 60")

print(timeInterval(startHour, startMinute, startSecond, endHour, endMinute, endSecond))
