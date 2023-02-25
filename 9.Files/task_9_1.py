# Напишите скрипт, который создаёт текстовый файл и записывает в него 10000 случайных действительных чисел.
# Создайте ещё один скрипт, который читает числа из файла и выводит на экран их сумму.
import random

num_list = ' '

for i in range(10000):
    number = random.randint(0, 1000)
    num_list += f'{str(number)} '
print(num_list)

with open("numbers.txt", "w") as file:
    file.write(num_list)

try:
    with open('numbers.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File doesn't exist.")

result = sum([int(i) for i in content.split()])
print(f"The sum of the range is {result}.")
