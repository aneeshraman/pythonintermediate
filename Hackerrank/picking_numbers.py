class PicckingNumbers:

    def __init__(self, a, n):
        self.array = a
        self.number_of_elements = n


n = int(input())

a = list(map(int, input().rstrip().split()))

result = PickingNumbers(a, n)
