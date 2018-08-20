separator = "~" * 45
print(separator)
# 04_home_task

# 0. #  Дан список чисел, заменить каждое число на квадрат этого числа.
# [1, 2, 3, 4] -> [1, 4, 9, 16]

list1 = [1, 2, 3, 4, 10]
print('before: ', list1)
for i in range(len(list1)):
    list1[i] = list1[i] ** 2

print('after:  ', list1)
print(separator)

# 1. Дан список чисел, заменить каждый отрицательный элемент на следующий
# [1, 2, -3, 5, -6, 7, -9] -> [1, 2, 5, 5, 7, 7, -9]

a = [1, 2, -3, 5, -6, 7, -9]
print('before: ', a)

for i in range(len(a)):
    if a[i] < 0 and i != len(a) - 1:
        a[i] = a[i + 1]
        # print(a[i])

print('after:  ', a)
print(separator)

# 2. Заменить каждый элемент на следующий, последний на первый
# [1, 2, 3, 4] -> [4, 1, 2, 3]

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
b = [0] * len(a)
print('before  :', a)
# print('before b :', b)

b[0] = a[-1]
for i in range(1, len(a)):
    if i != len(a):
        b[i] = a[i - 1]

print('after  : ', b)
print(separator)

# 3. Перевернуть список
# [1, 2, 3, 4] -> [4, 3, 2, 1]

b = [1, 2, 3, 4]
print(b)
c = list(reversed(b))
print(c)
print(separator)
