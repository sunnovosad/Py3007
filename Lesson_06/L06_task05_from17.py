"""
5. Найти сумму и произведение элементов одномерного числового списка.
"""


def get_sum(lst):
    return sum(lst)


def get_production(lst):
    m = 1
    for i in lst:
        m *= i
    return m


if __name__ == '__main__':
    assert get_sum([1, 2]) == 3
    assert get_sum([0, -3]) == -3

    assert get_production([1, 1]) == 1
    assert get_production([2, 3]) == 6
    assert get_production([0, 1]) == 0