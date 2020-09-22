import math


def squares(a, b):
    string_list = []
    range_list = []
    final_num = 0
    for range_element in range(a, b + 1):
        string_list.append(str(math.sqrt(range_element)))
        range_list.append(range_element)

    index_num = -1
    for string_list_element in string_list:
        index_num += 1
        if len(string_list_element) == 3:
            final_num += 1

    print(final_num)


q = int(input())

for q_itr in range(q):
    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    squares(a, b)
