# multiplication table output

# 1
# # Вложенные циклы L.2 p.20
# print('-' *30)

# for i in range(10):
#     for j in range(30):
#         print('*', end='')      # disable new line in print
#     print()                     # new line

print('-' *30)


# 2
# table
for i in range (1,11):
    for j in range(1,11):
        print(f'{i} x {j} = {i * j}')
    print()

print('-' *30)

#3
# Alternative view (from home taksks):
for a in range (1,10):
    for b in range(1, a + 1):
        print ('{}x{}={}\t'.format(a, b, a * b), end='')
    print()
print('-' *30)


