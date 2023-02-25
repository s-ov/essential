# Создайте 2 класса – языка, например, английский и испанский. У обоих классов должен быть метод greeting().
# Оба создают разные приветствия. Создайте два соответствующих объекта из двух классов выше и вызовите действия этих
# двух объектов в одной функции (функция hello_friend).
class English:
    def greeting(self):
        return f'Hello, friends!'


class Spanish:
    def greeting(self):
        return f'Hola, amigos!'


english = English()
spanish = Spanish()


def hello_friend():
    return f'{english.greeting()}\n{spanish.greeting()}'


print(hello_friend())
