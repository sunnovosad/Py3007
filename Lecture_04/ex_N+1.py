# break, continue, else  L.2 p.19

##1
##1  
# while условие:
#     блок_операторов_1
# else:
#     блок_операторов_2


#2
while True:
    response = input('Введите команду: ')
    if response == 'exit':
        break

print('-' *30)

#3
x = 0
while x < 10:
    x += 1
    if x == 5:
        continue
    print('текущее число равно:', x)
print ('Но число 5 мы здесь не выводим!')

print('-' *30)