# Создайте родительский(базовый) класс Vehicle, который имеет свойство vehicle_type = "none"
# Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию
# def horse_powers, которая возвращает количество лошадиных сил для автомобиля
# Создайте наследника класса Car и Vehicle - класс Nissan и переопределите свойство price и vehicle_type, а также
# переопределите функцию horse_powers
# Создайте экземпляр класса Nissan и распечатайте через функцию print vehicle_type, price


class Vehicle:
    vehicle_type = "none"


class Car:
    price = '1000000'

    def __init__(self, price):
        self.price = price

    def __str__(self):
        return '{} price {}'.format(self.__class__.__name__, self.price)

    def horse_powers(self):
        return 100


class Nissan(Vehicle, Car):

    def horse_powers(self):
        print('horse_powers 92')

    def vehicle_type(self):
        print('vehicle_type: sedan')



nissan = Nissan(price=900000)
print(nissan)
nissan.horse_powers()
nissan.vehicle_type()



