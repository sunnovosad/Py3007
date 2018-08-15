# 3
# Вывести таблицу умножения на экран.
# multiplication table in 5 x 2 classical view
header = "ТАБЛИЦА УМНОЖЕНИЯ"
print('{: ^77}'.format(header))
print('*' * 77)

for i in range (1,11):
    for j in range(1,6):
        print(f'{j} x {i} = {j * i}', end='\t\t')
    print()
print()
for i in range (1,11):
    for j in range(6,11):
        print(f'{j} x {i} = {j * i}', end='\t\t')
    print()

print('*' * 77)