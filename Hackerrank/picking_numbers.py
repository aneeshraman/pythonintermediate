class PickingNumbers:

    def __init__(self, a, n):
        self.array = a
        self.number_of_elements = n
    
    def difference_array(self):
        self.differenceArray = []
        self.array.sort(reverse=True)


n = int(input().strip())

a = list(map(int, input().rstrip().split()))

result = PickingNumbers(a, n)
