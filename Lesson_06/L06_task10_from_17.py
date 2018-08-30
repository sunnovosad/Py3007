"""
10. В одномерном списке удалить все четные элементы и оставить только нечетные.
"""


def odd(lst):
    b = []
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            b.append(lst[i])
    return b


if __name__ == '__main__':
    assert odd([1, 2, 3, 4]) == [1, 3]
    assert odd([0, 1, 1]) == [1, 1]

