#
# http://pythontutor.ru/lessons/lists/problems/same_sign_neighbours/   - тут тесты.
# v2 ...выведите только одну первую пару.
#

"""
7. Дан список чисел. Если в нем есть два соседних элемента одного знака,
выведите эти числа. Если соседних элементов одного знака нет — не выводите ничего.
Если таких пар соседей несколько — выведите первую пару.
"""


def find_pairs(lst):
    list = []
    for i in range(len(lst) - 1):
        if lst[i] > 0 and lst[i + 1] > 0:
            #print(lst[i], lst[i+1])
            list.append((lst[i], lst[i+1]))
            return list

        elif lst[i] < 0 and lst[i + 1] < 0:
            #print(lst[i], lst[i+1])
            list.append((lst[i], lst[i + 1]))
            return list

    return list

if __name__ == '__main__':
    assert find_pairs([1, 2, -1, -1]) == [(1, 2)]
    assert find_pairs([1, 2, 3, 4]) == [(1, 2)]
    assert find_pairs([1, -1, 2, -4]) == []
    # add tests:
    assert find_pairs([1, 2, 3, 4, -1, -6, 7, 98]) == [(1, 2)]
    assert find_pairs([1, -1, 1, -1, 1, 1, -1, 1, -1, 1]) == [(1, 1)]
    assert find_pairs([-1, -2, -3, -4]) == [(-1, -2)]

