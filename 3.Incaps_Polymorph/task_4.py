# Опишите два класса Base и его наследника Child с методами method(), который выводит на консоль фразы соответственно
# "Hello from Base" и "Hello from Child".
class Base:
    def method(self):
        return "Hello from Base"


class Child(Base):
    def method(self):
        return "Hello from Child"


base = Base()
child = Child()
print(base.method())
print(child.method())
