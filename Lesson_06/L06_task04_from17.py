"""
4. В списке найти минимальный и максимальный элементы, поменять их местами.
"""


def change_max_min(lst):
    min_elm = min(lst)
    max_elm = max(lst)
    #print(min_elm)
    #print(max_elm)
    a = lst.index(min_elm)
    b = lst.index(max_elm)
    lst[a], lst[b] = lst[b], lst[a]
    return lst


if __name__ == '__main__':
    assert change_max_min([1, 2, 3]) == [3, 2, 1]
    assert change_max_min([1, 1, 1]) == [1, 1, 1]
    assert change_max_min([2, 2, 1]) == [1, 2, 2]

# print()
# from random import randint
# c = [randint(-100, 100) for i in (range(11))]
# print(c)
# print(change_max_min(c))
