# examples_2_3\ex_2.py
users = ['Elias', 'Bob', 'Alex']

for user in users:
    print('Hello', user)

print ('------------------------')


# examples_2_3\ex_4.py
apples = [1, 124, 3623, 4, 223]
biggest_apple = apples[0]

for apple in apples:
    if apple > biggest_apple:
        biggest_apple = apple
print(biggest_apple)
print(max([1, 124, 3623, 4, 223]))          # max function
print(max(apples))          
print ('------------------------')

names = ['elias', 'alexander', 'bob', 'morten']
longest_name = names[0]

for name in names:
    if len(name) > len(longest_name):
        longest_name = name
print(longest_name)
print(max(names, key=len))                  # max by len  <--------------------****
print ('------------------------')
