"""
13. Дано два списка значений, вывести значения которые есть в обоих списках.
[1,2,3,4] [3, 5, 7, 1] -> [1, 3]
"""


def intersection_ordered(lst_1, lst_2):
    c = []
    for i in lst_1:
        if i in lst_2:
            c.append(i)
    return c


if __name__ == '__main__':
    assert intersection_ordered([1, 2, 3, 4], [3, 5, 7, 1]) == [1, 3]
    assert intersection_ordered([1, 2, 3], [3, 5, 4]) == [3]
    assert intersection_ordered([1, 2], [2, 1]) == [1, 2]
