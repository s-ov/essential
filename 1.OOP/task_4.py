# Создайте класс, описывающий автомобиль. Создайте класс автосалона, содержащий в себе список автомобилей,
# доступных для продажи, и функцию продажи заданного автомобиля.
class Cars:
    def __init__(self, type_, engine_type, volume, power):
        self.type_ = type_
        self.engine = engine_type
        self.power = power
        self.volume = volume
        self.car = CarDealership()

    def __repr__(self):
        return f"{self.car.sell_car()}:\n{self.type_}/{self.engine}/{self.power}/{self.volume}"


class CarDealership:
    def __init__(self):
        self.car_list = ['WV', 'BMW', 'MG']

    def choose_car(self):
        car_choice = input(f'Choose a car code in the range:\n{[str(i) for i in range(len(self.car_list))]} - ')
        if car_choice not in [str(i) for i in range(len(self.car_list))]:
            return f'No such brand.'
        return car_choice

    def sell_car(self):
        return f'{self.car_list[int(self.choose_car())]} is sold'


car1 = Cars('sedan', 'diesel', 2.0, '140PS')
car2 = Cars('SUV', 'gasoline', 3.0, '185PS')
car3 = Cars('hatchback', 'hybrid', 1.6, '105PS')
for car in [car1, car2, car3]:
    print(car.__repr__())
