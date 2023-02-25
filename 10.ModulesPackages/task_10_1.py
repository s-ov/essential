# Перепишите домашнее задание предыдущего урока (сервис для сокращения ссылок) таким образом, чтобы у него была основная
# часть, которая отвечала бы за логику работы и предоставляла обобщённый интерфейс, и модуль представления, который
# отвечал бы за взаимодействие с пользователем. При замене последнего на другой, взаимодействующий с пользователем иным
# способом, программа должна продолжать корректно работать.
def input_data(arg1, arg2):
    with open('staff_list.txt', 'a') as file:
        file.write(f"Surname: {arg1}; Info: {arg2}\n")
    return file


def output_data():
    try:
        with open('staff_list.txt') as file:
            for line in file:
                print(line)
    except FileNotFoundError:
        print("File not found.")


def add_data(dict_, key, value):
    dict_[key] = value
    return dict_
