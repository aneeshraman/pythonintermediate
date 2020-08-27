class PickingNumbers:
    def __init__(self, a, n):
        self.indexList = []
        self.differenceArray = []
        self.array = a
        self.number_of_elements = n

    def difference_array(self):
        self.array.sort(reverse=True)
        indexNumber = -1
        for i in self.array:
            indexNumber += 1
            y = self.array[indexNumber + 1]
            self.differenceArray.append(y - i)

    def analyse(self):
        indexNumber = -1
        for i in self.differenceArray:
            indexNumber += 1
            if i == 1 or i == 0:
                self.indexList.append(indexNumber)
                self.indexList.append(indexNumber + 1)

        self.indexList = list(dict.fromkeys(self.indexList))

        print(len(self.indexList))


n = int(input().strip())

a = list(map(int, input().rstrip().split()))

result = PickingNumbers(a, n)
result.difference_array()
result.analyse()
