# Algorithm
# We would repeat the process of getting the minimum element and then popping that element out

def sortArray(array):
    resultArray = []
    for i in range(len(array)):
        resultArray.append(min(array))
        array.remove(min(array))

    return resultArray


inputArray = input("Enter an array\n").rstrip().split()
print("The result is: ", sortArray(inputArray))
