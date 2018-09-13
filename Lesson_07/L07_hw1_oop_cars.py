# 1.0 Создать класс Автомобиль содержащий информацию: модель, цвет, год_выпуска, стоимость. Описать метод __str__.
# Пример
# >> car1 = Car(‘Audi’, ‘Red’, ‘1999’, ‘$12000’)
# >>print(car1)
# name: Audi
# color: Red
# year: 1999
# price: $12000
#
# 1.1 Создать класс Автосалон содержащий информацию: адрес, имя, список доступных машин.
# Реализовать методы для отображения всех доступных машин, добавления новых машин, покупки машин (после покупки машина удаляется из списка) + проверки на наличие такой машины в салоне
# Пример
# >> car1 = Car(‘Audi’, ‘Red’, ‘1999’, ‘$12000’)
# >> car2 = Car(‘BMW’, ‘Black’, ‘2009’, ‘$18000’)
# >>
# >>showroom = ShowRoom(‘Borshagovska 17’, ‘Volkswagen showroom’)
# >>showroom.add_car(car1)
# >>showroom.add_car(car2)
# >>
# >>showroom.show_all()
# 1
# ————————-
# name: Audi
# color: Red
# year: 1999
# price: $12000
#
# 2
# —————————
# name: BMW
# color: Black
# year: 2009
# price: $18000
# >>showroom.sell_car(Car(‘Volvo’, ‘Red’, ’1993’, ‘$20000’))
# ‘No such car!’
# >>showroom.sell_car(car1)
# ‘Car has been sold!’
# >>showroom.show_all()
# 1
# —————————
# name: BMW
# color: Black
# year: 2009
# price: $18000
print('~' * 50)

# Cars Class


class Cars:
    def __init__(self, model='n/a', color='default white', year =2018, cost=10000):
        self.model = model
        self.color = color
        self.year = year
        self.cost = cost

    def __str__(self):
        return f'Model: {self.model}\nColor: {self.color}\n' \
               f'Year: {self.year}\nPrice: ${self.cost}\n'

    def __eq__(self, other):
        # Variant_1
        same_car = (self.model == other.model and
                    self.color == other.color and
                    self.year == other.year and
                    self.cost == other.cost
                    )
        return same_car
        # Variant_2
        #return self.__dict__ == other.__dict__


car1 = Cars('Audi', 'Red', 1999, 10000)
car2 = Cars('Skoda', 'White', 2014, 15000)
car3 = Cars('BMW', 'Black', 2009, 8000)
car4 = Cars('Volvo', 'Red', 1993, 2000)
car5 = Cars('Skoda', 'White', 2014, 15000)   # car5 the same as car2
#...

print(car1)
print(car2)
print('~' * 50)

# Automobile sales centre AutoCentre


class ShowRoom:
    def __init__(self, address, name, car_list =[]):
        self.address = address
        self.name = name
        self.car_list = car_list

    def __str__(self):
        return f'AutoCentre: {self.name} on {self.address}'

    def add_car(self, car):
        self.car_list.append(car)

    def show_all(self):
        if self.car_list:
            #print(self.car_list)
            count_show = 1
            underline = '_' *15
            print('Cars in showroom:')
            for i in self.car_list:
                print(count_show)
                print(underline)
                print(i)
                count_show +=1
        else:
            print ('No cars left in AutoCentre.')

    def sell_car(self, car):
        #print(self.car_list)
        #print(car in self.car_list)
        if car in self.car_list:
            self.car_list.remove(car)
            print('This', car.model, 'has been sold!')
        else:
            print('No such car in showroom.')


showroom = ShowRoom('Borshagovska Str. 17', 'Volkswagen showroom')
print(showroom)
print('~' * 50)

# before
showroom.show_all()
print('~' * 50)

#add_1
showroom.add_car(car1)   # car1 = Cars('Audi', 'Red', 1999, 10000)
showroom.show_all()
print('~' * 50)
# add_2
showroom.add_car(car2)   # car2 = Cars('Skoda', 'White', 2014, 15000)
showroom.show_all()
print('~' * 50)


# sell_1
print('Sell_1')
showroom.sell_car(car3)
#showroom.show_all()
print('~' * 50)

# sell_2 (new object, but the same car)
#print(car2)
print('~' * 50)
#showroom.sell_car(car2)
print('Sell_2:')
showroom.sell_car(Cars('Skoda', 'White', 2014, 15000))  # <---new obj
print('~' * 50)

showroom.show_all()
print('~' * 50)

# sell_3
print('Sell_3')
showroom.sell_car(car1)
print('~' * 50)
showroom.show_all()
print('~' * 50)

# sell_4
print('Sell_4:')
showroom.add_car(car2)  # car2
showroom.show_all()
showroom.sell_car(car5) # car5
showroom.show_all()
print('~' * 50)

