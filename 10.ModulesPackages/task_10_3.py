# Создайте модуль для получения простых чисел. Импортируйте его из другого модуля. Импортируйте отдельные его имена.
import module_10_3

while True:
    menu = input("Menu:\n1.Option gets prime numbers up to some number.\n"
                 "2.Option gets some number of prime numbers.\n3.Exit.\n"
                 "Choose 1, 2 or 3: ")
    if menu not in ['1', '2', '3']:
        print(f"'{menu}': no such menu item.")
        continue
    elif menu == '3':
        print("Program is closes.")
        break
    number = input("Enter a number to what you wanna get prime numbers or how many prime numbers to get: ")
    try:
        number = int(number)
    except ValueError:
        print(f"ValueError: '{number}' isn't integer!")
        continue
    if menu == '1':
        print(list(module_10_3.get_primes(number)))
    elif menu == '2':
        print(list(module_10_3.get_n_primes(number)))
