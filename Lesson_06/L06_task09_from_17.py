"""
9. Из одномерного списка удалить все повторяющиеся элементы (дубликаты) так,
чтобы каждое значение встречалось в списке только один раз.
"""

def uniq_list(lst):
    c =[]
    for i in lst:
        if i not in c:
            c.append(i)
    return c


if __name__ == '__main__':
    assert uniq_list([1, 1, 2]) == [1, 2]
    assert uniq_list([1, 2, 2, 3, 4, 4, 5, 6, 7, 7]) == [1, 2, 3, 4, 5, 6, 7]
    assert uniq_list(['a', 'a', 'a', 'af', 'h', 'k', 'k']) == ['a', 'af', 'h', 'k']
    assert uniq_list([[1, 2], [1, 2], 3, 4, 4, 'oops', 'oops']) == [[1, 2], 3, 4, 'oops']
