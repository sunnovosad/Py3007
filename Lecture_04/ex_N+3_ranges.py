#1
for i in range(3):
    print('*',i)

print ('------------------------')

#2
for i in range(11):
    print(i)

print ('------------------------')

#3
for i in range(10,21):
    print(i)

print ('------------------------')


#4
for i in range(1,20,2):   # все нечетные числа, 1, 1+2,....
    print(i)

print ('------------------------')


#5
for i in range(1,20,1000):   # только первое число
    print(i)

print ('------------------------')

#6
a = range (1,3)
print (a)
young = range(6,19)
age = 8
if age in young:
    print ('hello!!')

print ('------------------------')


# >>> range(10)
# range(0, 10)
# >>> print(range(10))
# range(0, 10)
# >>> list(_)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> reversed(_)
# <list_reverseiterator object at 0x000001A3DB6E50F0>
# >>> list(_)
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# >>> 
# >>> list(reversed(range(10)))             # reversed example
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# >>> list (range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> 



# Lists...
# the same list in list
b = [1, 12, 'fsgsefwe', None, [1,2,3]]
print(b)
b.append(b)
print(b)                # [1, 12, 'fsgsefwe', None, [1, 2, 3], [...]]
print ('------------------------')
for element in b:
    print (element)

print ('------------------------')











