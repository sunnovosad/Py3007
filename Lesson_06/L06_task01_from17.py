"""
1. Найти номер и значение первого положительного элемента списка.
"""


def find_first_positive(lst):
    for i in range(len(lst)):
        if lst[i] > 0:
            result = (i, lst[i])
            return result


if __name__ == '__main__':
    # some tests
    assert find_first_positive([-1, 2, 5]) == (1, 2)
    assert find_first_positive([1, 2, 5]) == (0, 1)
    assert find_first_positive([-1, -2, 5]) == (2, 5)
    assert find_first_positive([-1, -2, -5]) is None