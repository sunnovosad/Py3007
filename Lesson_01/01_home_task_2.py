# 2. Вычислить возраст человека. Программа принимает с клавиатуры год рождения 
# и выводит возраст на экран.
# Пример:
# Ваша дата рождения:
# 1990
# Вам 28 лет
#

import datetime
#examples
#print("Current date and time: ", datetime.datetime.now())
#a = datetime.datetime.today().year
#b = datetime.datetime.now().year 
#c =  datetime.date.today().year

current_year = datetime.date.today().year
birth_year = int(input('Ваша дата рождения (укажите год): '))
your_age =  current_year - birth_year
print('Вам', your_age, 'лет/год(а).')






