separator = "~" * 60
print(separator)
# 04_home_task

# 4. Заменить элементы с нечетными номерами на 0
# 	[1, 1, 1, 1, 1] -> [1, 0, 1, 0, 1]

# 4
mylist = [1, 1, 1, 1, 1]
print('Before:', mylist)

for i in range(len(mylist)):
    if i % 2 != 0:
        mylist[i] = 0

print('After: ', mylist)
print(separator)


# 5. Посчитать сумму первых двух четных чисел в списке
# 	[5, 7, 8, 3, 4, 6, 8] -> 12
my_list_1 = [5, 7, 8, 3, 4, 6, 8]
qty_1 = 1
sum_1 = 0

for i in range(len(my_list_1)):
    if my_list_1[i] % 2 == 0 and qty_1 <= 2:
        qty_1 += 1
        sum_1 += my_list_1[i]

print('My list:', my_list_1)
print("Cумма первых двух четных чисел:", sum_1)
print(separator)


# 6. Дан список строк. Посчитать количество символов в первой строке где есть символ ‘а’.
# 	[‘‪fur’, ‘skin’, ‘coat’, ‘pelage’, ‘jack‬’] -> 4 # len(‘coat’)

#6
my_list_str = ['fur', 'skin', 'coat', 'babon', 'pelage', 'jack']
print('My list:', my_list_str)
for i in my_list_str:
    if 'a' in i:
        len_str = len(i)
        print('Len is:', len_str, 'and str was:', i)
        break
print(separator)



