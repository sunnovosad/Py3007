# 5
# 5. Напишите программу, запрашивающую имя, фамилия, отчество и номер группы студента и выводящую введённые данные в следующем виде:
#  ************************************
#  *Лабораторная работа № 1   *
#  *Выполнил(а): ст. гр. ЗИ-123 *
#  *Иванов Андрей Петрович    *
#  ************************************
# Необходимо, чтобы программа сама определяла нужную длину рамки.
# Сама же длина рамки зависит от длины наибольшей строки внутри рамки. Используя циклы for легко можно выровнять стороны рамки.

LINE1 = "Лабораторная работа N 1"
LINE2 = "Выполнил(а): ст. гр. "
len_line1 = len(LINE1)
len_line2 = len(LINE2)

group = input("Введите номер группы: ")
name = input("Введите ваше ФИО: ")
len_group = len(group)
len_name = len(name)

# check_1
# print('len_line1', len_line1)
# print('len_line2', len_line2)
# print('len_group', len_group)
# print('len_name', len_name)


len_max = max(len_line1, (len_line2 + len_group), len_name)
# print('len_max=',len_max)
print()

# spaces
# corr = 1
len_space1 = len_max - len_line1
len_space2 = len_max - len_line2 - len_group
len_space3 = len_max - len_name

space_line1 = ' ' * len_space1
space_line2 = ' ' * len_space2
space_line3 = ' ' * len_space3

# output
border_line = '*' * (len_max +2)

print(border_line)
print('*' + LINE1 + space_line1 + '*')
print('*' + LINE2 + group + space_line2 + '*')
print('*' + name + space_line3 + '*')
print(border_line)

# check_2
# print(len(border_line))
# print(len('*' + LINE1 + space_line1 + '*'))
# print(len('*' + LINE2 + group + space_line2 + '*'))
# print(len('*' + name + space_line3 + '*'))
