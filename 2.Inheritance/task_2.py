class Rectangle:
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width

    def make_rectangle(self):
        for item in range(self.width):
            print("*" * self.length)


class Button:
    @staticmethod
    def click_button(rect):
        return Rectangle.make_rectangle(rect)


if __name__ == '__main__':
    rectangle = Rectangle(8, 4)
    button = Button()
    user_choice = input("""Do you want to see the figure?\nIf yes - click 'y', if no - any button: """)
    if user_choice != "y":
        print("Sorry for your decision. Bye-bye!")
        exit()
    button.click_button(rectangle)

