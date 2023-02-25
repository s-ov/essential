# Создайте функцию от произвольного количества аргументов, которая вычисляет среднее арифметическое данных чисел.
# Вычислите при помощи неё среднее арифметическое двух заданных чисел и среднее арифметическое чисел
# из заданного диапазона.
def calc_average(*args):
    if len(args[0]) == 0:
        return 'Error: empty list is not allowed.'
    return round(sum(args[0]) / len(args[0]), 2)


if __name__ == '__main__':
    while True:
        first_num = input('Enter first number: ')
        second_num = input('Enter second number greater than first: ')
        try:
            first_num = int(first_num)
            second_num = int(second_num)
            break
        except ValueError:
            print('ValueError: first and second numbers must be integer.')
        finally:
            if first_num > second_num:
                print('OrderError: second number must be greater than first.')
                continue
            else:
                pass

    print(f'Average of {list(range(first_num, second_num))}', end=' - ')
    print(calc_average(range(first_num, second_num)))
