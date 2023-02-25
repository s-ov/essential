# Опишите свой класс исключения. Напишите функцию, которая будет выбрасывать данное исключение, если пользователь
# введёт определённое значение, и перехватите это исключение при вызове функции.
class MyException(Exception):
    pass


money = input('Enter a sum to make you happy: ')
try:
    money = float(money)
except:
    raise MyException('Error! Enter only numeric data.')

print(f'The sum {money} can make you happy')



