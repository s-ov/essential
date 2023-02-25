# Создайте иерархию классов с использованием множественного наследования. Выведите на экран порядок разрешения методов
# для каждого из классов. Объясните, почему линеаризации данных классов выглядят именно так.
class Animals:
    pass


class Horse(Animals):
    pass


class Donkey(Animals):
    pass


class Mule(Donkey, Horse):
    pass


print(Animals.__mro__)
print(Horse.__mro__)
print(Donkey.__mro__)
print(Mule.__mro__)
