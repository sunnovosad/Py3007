"""
2. Найти сумму положительных элементов списка.
"""


def sum_of_positives(list):
    sum = 0
    for i in range(len(list)):
        if list[i] > 0:
            sum += list[i]
    return sum


if __name__ == '__main__':
    assert sum_of_positives([1, 2, -4, 0]) == 3
    assert sum_of_positives([-1, -2, -3]) == 0
    assert sum_of_positives([1, 1, 1]) == 3