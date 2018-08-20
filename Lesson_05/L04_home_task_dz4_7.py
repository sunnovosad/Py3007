separator = "~" * 45
print(separator)
# 04_home_task

# 7*. Отсортировать список методом пузырьковой сортировки.

# 7.1
# list = [0, 5, 8, 4, 9, 3]
list = [101, 20, 30, 5, 6, 7, 200, 34, 45, -10]
print('Initial list:  ', list)
print()

for j in range(len(list) - 1):
    for i in range(len(list) - j - 1):
        # the number of comparisons each time decreases by j
        if list[i] > list[i + 1]:
            list[i], list[i + 1] = list[i + 1], list[i]
            # print(list)
    print(f'{j + 1}-d cycle pass:', end=" ")
    print(list)

print()
print('Sorted list:   ', list)
print(separator)


# 7.2
# by function

def bubble_sort(mylist):
    for pass_num in range(len(mylist) - 1, 0, -1):
        for i in range(pass_num):
            if mylist[i] > mylist[i + 1]:
                mylist[i], mylist[i + 1] = mylist[i + 1], mylist[i]

mylist1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(mylist1)

bubble_sort(mylist1)

print(mylist1)
print(separator)

