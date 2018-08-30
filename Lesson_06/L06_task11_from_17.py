"""
11. Дан список значений. Превратить список в словарь где ключами служат
элементы списка, а значениями квадраты этих элементов.
[1,2,3] -> {1:1, 2:4, 3:9}
"""


def list_to_dict(lst):
    key = []
    value = []
    for i in range(len(lst)):
        key.append(lst[i])
        value.append((lst[i]**2))
    #print(key)
    #print(value)
    return dict(zip(key, value))


if __name__ == '__main__':
    assert list_to_dict([1, 2, 3]) == {1: 1, 2: 4, 3: 9}
