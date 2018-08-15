# 0.0 
# Вывести на экран все числа в диапазоне от 10 до 20
for i in range(10, 21):
    print(i)

print('*' * 30); print()


# 0.1
# Спросить у пользователя два числа: a и b, вывести все числа в диапазоне от a до b.
a = int(input('Enter number a: '))
b = int(input('Enter number b: '))
print('Range for [a, b] will be: ')
for i in range(a, b + 1):
    print(i, end=' ')

print()
print('*' * 30); print()

# 0.2 v.2
# 0.2. Спросить у пользователя сколько ему лет. Если ему:
# от 1 до 5 вывести "Пливет"
# от 6 до 18 вывести "Йо!"
# от 19 до 40 вывести "Привет"
# от 41 до 100 вывести "Здравствуйте!"
# больше 100 вывести "Ого!"

age = (input('How old are you? '))
print(age)

range_1 = range(0, 6)  # от 1 до 5 вывести "Пливет"
range_2 = range(6, 19)  # от 6 до 18 вывести "Йо!"
range_3 = range(19, 41)  # от 19 до 40 вывести "Привет"
range_4 = range(41, 101)  # от 41 до 100 вывести "Здравстуйте!"

if age:
    age = int(age)
    if age in range_1:
        print("Пллливет!")
    elif age in range_2:
        print("Йо!")
    elif age in range_3:
        print("Привет!")
    elif age in range_4:
        print("Здравствуйте!")
    else:
        print("Ого!")
