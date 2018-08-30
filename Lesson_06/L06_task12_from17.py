"""
12. Дан список значений. Превратить список в словарь
поочередно превращая елменты в ключи и значения.
[1, 2, 3, 4, 5, 6] -> {1: 2, 3: 4, 5: 6}
"""


def list_to_dict(lst):
    b = []
    for i in range(int(len(lst) / 2)):
        # print(i)
        b.append((lst[0 + 2 * i], lst[1 + 2 * i]))
    #print(b)
    return dict(b)


if __name__ == '__main__':
    assert list_to_dict([1, 2, 3, 4, 5, 6]) == {1: 2, 3: 4, 5: 6}
    assert list_to_dict([1, 2, 3, 4, 5]) == {1: 2, 3: 4}
    assert list_to_dict(['k', 'v', 'k2', 'v2']) == {'k': 'v', 'k2': 'v2'}
