def sort(array):
    sortArray = []
    while len(array) != 0:
        sortArray.append(min(array))
        array.remove(min(array))

    return sortArray


inputArray = input("Enter a array with each element separated with space: ").split()
for index in range(len(inputArray)):
    inputArray[index] = int(inputArray[index])
print(sort(inputArray))
