# Используя ссылки в конце данного урока, ознакомьтесь с таким средством инкапсуляции как свойства.
# Ознакомьтесь с декоратором property в Python. Создайте класс, описывающий температуру и позволяющий задавать и
# получать температуру по шкале Цельсия и Фаренгейта: данные могут быть заданы в одной шкале, а получены в другой.
# t_F = t_C * 1.8 + 32; t_C = (t_F - 32) / 1.8
class TemperatureConvertor:
    def __init__(self, grades):
        self.__grades = grades

    @property
    def grade(self):
        return self.__grades

    @grade.setter
    def grade(self, grade):
        self.__grades = grade

    def celsius_to_fahrenheit(self):
        return round((self.__grades - 32) / 1.8, 1)

    def fahrenheit_to_celsius(self):
        return round(self.__grades * 1.8 - 32, 1)


convertor = TemperatureConvertor(0)
print(convertor.celsius_to_fahrenheit())
print(convertor.fahrenheit_to_celsius())
convertor.grade = 10
print(convertor.grade)
