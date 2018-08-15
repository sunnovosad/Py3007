# 2
# Составить алгоритм увеличения всех трех, введённых с клавиатуры, переменных на 5,
# если среди них есть хотя бы две равные. В противном случае выдать ответ «равных нет».
a = int(input('A: '))
b = int(input('B: '))
c = int(input('С: '))
print('Your Numbers: A, B, C: ', a, b, c)

if a == b or a == c or  b == c:
    a += 5; b += 5; c += 5
    print(f'Increased by 5: A = {a}, B = {b}, C = {c}.')
else:
    print('There are no equal.')

print('*' * 30); print()
