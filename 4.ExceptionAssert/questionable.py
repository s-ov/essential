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
        if self._number_2 == 0:
            return f'Denominator must be different of zero'
        return self._number_1 / self._number_2

    def raise_to_power(self):
        return self._number_1 ** self._number_2


if __name__ == '__main__':
    print("Hello! You're in Calculator.")

    def shut_calculator():
        print('Bye-bye!')
        exit()

    def enter_option():
        while True:
            math_option = input("Enter any option of these: +, -, *, /, ** or 'exit' to exit calculator: ")
            if math_option == 'exit':
                shut_calculator()
            if math_option in ['+', '-', '*', '/', '**']:
                break
            else:
                print("Incorrect input. Try again.")
        return math_option


    def enter_number1():
        while True:
            try:
                first_number = float(input('Enter first number or "exit" to be quit: '))
                break
            except ValueError:
                print("Value error! Try again.")
            return first_number


    def enter_number2():
        while True:
            try:
                second_number = float(input('Enter second number or "exit" to be quit: '))
                break
            except ValueError:
                print("Value error! Try again.")
        return second_number

    result = Calculator(enter_number1(), enter_number2())


    def mainloop():
        if enter_option() == '+':
            print(result.add_numbers())
        elif print(enter_option()) == '-':
            print(result.subtract_numbers())
        elif print(enter_option()) == '*':
            print(result.multiply_numbers())
        elif print(enter_option()) == '/':
            print(result.divide_numbers())
        elif print(enter_option()) == '**':
            print(result.raise_to_power())
        elif print(enter_option()) == 'exit':
            shut_calculator()

    while True:
        enter_option()
        enter_number1()
        enter_number2()
        mainloop()
        # shut_calculator = input("Type 'exit' if you need to shut down the calculator or any key to continue: ")
        # if shut_calculator == 'exit':
        #     shut_calculator()
        # else:
        #     mainloop()