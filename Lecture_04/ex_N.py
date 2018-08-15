# Проверки.... from ex_0.py

# Логически значения объектов L.2 p.16
# None, False, 0, 0.0, 0j, ‘’(пустая строка), [], {} == False
# Все остальное (для перечисленных типов) == True

#
string = 'abc'
if string is not None and string !='':
    num = int(string)

if string:
    num = int(string)

#
name = input('Name? ')
if name:
    print ('Hello', name)

print('-' *30)


# 
a = 5

while a:
    print(a)
    a -= 1
print('-' *30)


##
for i in range(-5, 5):
    #print('i=',i)
    if i == 0:
        print('pass div by',i)
        continue
    print(1 / i)

print('-' *30)
# ##
# for i in range(-5, 5):
#     if i != 0:
#         continue
#     print ('zero catch:', i)
#     print(1 / i)

# print('-' *30)


#
a = ['elias', 'pedro', 'pablo', '....']
if a:
    for element in a:
        print(element)

print('-' *30)

