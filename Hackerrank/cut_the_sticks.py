# Algorithm
# First, we would create a algo for removing out the lowest element
def one_iter(array):
    array.sort()
    length_of_cut = array[0]
    array = list(map(lambda a: a - length_of_cut, array))

    array = list(filter(lambda a: a != 0, array))

    return array


def cutTheSticks(array):
    print(len(array))
    while len(array) > 1:
        array = one_iter(array)
        if len(array) > 0:
            print(len(array))


n = int(input())

arr = list(map(int, input().rstrip().split()))

cutTheSticks(arr)
