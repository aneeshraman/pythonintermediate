import math


def squares(a, b):
    string_list = []
    range_list = []
    for range_element in range(a, b + 1):
        string_list.append(str(math.sqrt(range_element)))
        range_list.append(range_element)


q = int(input())

for q_itr in range(q):
    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    squares(a, b)
