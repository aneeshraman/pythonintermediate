import math


def squares(a, b):
    final_num = 0
    square_list = []
    for i in range(1, (10 ** 5) + 1):
        square_list.append(i ** 2)

    for i in square_list:
        if a <= i <= b:
            final_num += 1

    print(final_num)


q = int(input())

for q_itr in range(q):
    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    squares(a, b)
