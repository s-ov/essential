# Напишите программу-калькулятор, которая поддерживает следующие операции: сложение, вычитание, умножение, деление и
# возведение в степень. Программа должна выдавать сообщения об ошибке и продолжать работу при вводе некорректных данных,
# делении на ноль и возведении нуля в отрицательную степень.
class Calculator:
    def __init__(self, number_1, number_2):
        self._number_1 = number_1
        self._number_2 = number_2

    def add_numbers(self):
        return self._number_1 + self._number_2

    def subtract_numbers(self):
        return self._number_1 - self._number_2

    def multiply_numbers(self):
        return self._number_1 * self._number_2

    def divide_numbers(self):
        while self._number_2 == 0:
            return f'Denominator must be different of zero'
        return self._number_1 / self._number_2

    def raise_to_power(self):
        return self._number_1 ** self._number_2


if __name__ == '__main__':
    print("Hello! You're in Calculator.")

    def shut_calculator():
        print('Bye-bye!')
        exit()


    while True:
        math_option = input("Enter any option of these: +, -, *, /, ** or 'exit' to exit calculator: ")
        if math_option == 'exit':
            shut_calculator()
        if math_option in ['+', '-', '*', '/', '**']:
            break
        else:
            print("Incorrect input. Try again.")

    while True:
        try:
            first_number = float(input('Enter first number or "exit" to be quit: '))
            break
        except ValueError:
            print("Value error! Try again.")

    while True:
        try:
            second_number = float(input('Enter second number or "exit" to be quit: '))
            break
        except ValueError:
            print("Value error! Try again.")

    result = Calculator(first_number, second_number)


    def mainloop():
        if math_option == '+':
            print(result.add_numbers())
        elif math_option == '-':
            print(result.subtract_numbers())
        elif math_option == '*':
            print(result.multiply_numbers())
        elif math_option == '/':
            print(result.divide_numbers())
        elif math_option == '**':
            print(result.raise_to_power())
        elif math_option == 'exit':
            shut_calculator()

    mainloop()




