# Опишите классы графического объекта, прямоугольника и объекта, который может обрабатывать нажатия мыши. Опишите класс
# кнопки. Создайте объект кнопки и обычного прямоугольника. Вызовите метод нажатия на кнопку.
class Figure:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def make_me(self):
        for item in range(self.width):
            print("*" * self.length)
        return f'Here I am with length {self.length} and width {self.width}'


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__(length, width)


class MouseHandler:
    def __init__(self):
        self.obj = Rectangle(x=0, y=0)

    def set_mouse(self):
        return self.obj.make_me()


class Button:
    def __init__(self):
        self.mouse = MouseHandler()

    def click_button(self):
        return self.mouse.set_mouse()


rect = Figure(8, 4)
# print(rect.make_me())
button = Button()
mouse = MouseHandler()

print("Do you want to see the figure?")
user_choice = input("If yes - click 'y', if no - any button: ")
if user_choice != "y":
    print("Sorry for your decision. Bye-bye!")
    exit()
else:
    mouse.set_mouse()
