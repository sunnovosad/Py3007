"""
7. Дан список чисел. Если в нем есть два соседних элемента одного знака,
выведите эти числа. Если соседних элементов одного знака нет — не выводите ничего.
Если таких пар соседей несколько — выведите первую пару.
"""

def find_pairs(lst):

    # step_1
    lst_c = []
    for i in range(len(lst) - 1):
        if lst[i] > 0 and lst[i+1] > 0 or lst[i] < 0 and lst[i+1] < 0:
            lst_c.append((lst[i], lst[i+1]))
    #print(lst_c)

    # step_2
    lst_d = []
    for i in range(len(lst_c) - 1):
        if sum(lst_c[i]) > 0 and sum(lst_c[i+1]) > 0 or sum(lst_c[i]) < 0 and sum(lst_c[i+1]) < 0:
            lst_d.append(lst_c[i + 1])
    #print(lst_d)

    # step_3
    for i in lst_d:
        #print(i)
        lst_c.remove(i)

    return lst_c

if __name__ == '__main__':
    assert find_pairs([1, 2, -1, -1]) == [(1, 2), (-1, -1)]
    assert find_pairs([1, 2, 3, 4]) == [(1, 2)]
    assert find_pairs([1, -1, 2, -4]) == []
    # add tests:
    assert find_pairs([1, 2, 3, 4, -1, -6, 7, 98]) == [(1, 2), (-1, -6), (7, 98)]
    assert find_pairs([1, -1, 1, -1, 1, 1, -1, 1, -1, 1]) == [(1, 1)]
