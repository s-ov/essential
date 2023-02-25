# Создайте словарь с ключами-строками и значениями-числами. Создайте функцию, которая принимает произвольное количество
# именованных параметров. Вызовите её с созданным словарём и явно указывая параметры.
number_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}


def get_dict_value(**kwargs):
    for key, value in kwargs.items():
        print(f'key = {key}; value = {value}')


if __name__ == '__main__':
    get_dict_value(**number_dict)
