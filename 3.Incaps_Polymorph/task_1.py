# Создайте класс, описывающий автомобиль. Какие атрибуты и методы должны быть полностью инкапсулированы?
# Доступ к таким атрибутам и изменение данных реализуйте через специальные методы (get, set).
class Car:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year


class UpdateCar(Car):
    def __init__(self, brand, color, year, price):
        super().__init__(brand, color, year)
        self._price = price

    def _get_brand(self):
        return self.brand

    def _get_color(self):
        return self.color

    def _get_year(self):
        return self.year

    def _get_price(self):
        return self._price

    def _set_brand(self, new_brand):
        self.brand = new_brand

    def _set_color(self, new_color):
        self.color = new_color

    def _set_year(self, another_year):
        self.year = another_year

    def _set_price(self, new_price):
        self._price = new_price

    def __get_info(self):
        return f'Brand: {self._get_brand()}, color: {self._get_color()}, Year of Manufacturing: {self._get_year()} '\
                f'Price: {self._get_price()}'

    def show_info(self):
        return self.__get_info()


car_1 = UpdateCar('VW', 'grey', '2001', 3600)
car_2 = UpdateCar('Volvo', 'green', '2011', 6600)
car_3 = UpdateCar('BMW', 'black', '2014', 8100)
cars = [car_1, car_2, car_3]
update_menu = input("You are in update menu: push 'y' to continue or any button to exit: ")
while update_menu == 'y':
    which_car = int(input(f'Choose order number of car{[i for i in range(len(cars))]}: '))
    if which_car not in [i for i in range(len(cars))]:
        print('Incorrect input.')
        continue
    parameter = input("Choose parameter to edit: 1 -brand, 2 - color, 3 - year, 4 - price: ")
    if parameter == '1':
        user_input = input('Enter brand name: ')
        car_1._set_brand(new_brand=user_input)
    elif parameter == '2':
        user_input = input('Enter color name: ')
        cars[which_car]._set_color(new_color=user_input)
    elif parameter == '3':
        user_input = input('Enter year of manufacturing: ')
        cars[which_car]._set_year(another_year=user_input)
    elif parameter == '4':
        user_input = int(input('Enter new price: '))
        cars[which_car]._set_price(new_price=user_input)
    print(cars[which_car].show_info())
    update_menu = input("You are in update menu: push 'y' to continue or any button to exit: ")
