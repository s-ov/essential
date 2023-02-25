# Создайте иерархию классов транспортных средств. В общем классе опишите общие для всех транспортных средств поля,
# в наследниках специфичные для них. Создайте несколько экземпляров. Выведите информацию о каждом транспортном средстве.
class Vehicle:
    def __init__(self, name, speed, wheels):
        self.name = name
        self.speed = speed
        self.wheels = wheels

    def show_info(self):
        return f'Name: {self.name}\nSpeed: {self.speed}\nWheels: {self.wheels}\n'


class Car(Vehicle):
    def __init__(self, name, speed, wheels, motor):
        self.motor = motor
        super().__init__(name, speed, wheels)

    def show_info(self):
        return super().show_info() + f'Motor: {self.motor}'


class Boat(Vehicle):
    def __init__(self, name, speed, propeller):
        self.propeller = propeller
        super().__init__(name, speed, wheels=0)

    def show_info(self):
        return super().show_info() + f'Propeller: {self.propeller}'


class Bike(Vehicle):
    def __init__(self, name, speed, wheels, saddle):
        self.saddle = saddle
        super().__init__(name, speed, wheels)

    def show_info(self):
        return super().show_info() + f'Saddle: {self.saddle}'


car = Car('Volvo', '240km/h', 4, 'diesel, 210PS')
boat = Boat('Yamaha', '140km/h', 'Small propeller')
bike = Bike('Crosser', '45km/h', 2, 'cosy')
print(car.show_info())
print(boat.show_info())
print(bike.show_info())
