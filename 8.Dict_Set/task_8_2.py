# Создайте программу, которая эмулирует работу сервиса по сокращению ссылок. Должна быть реализована возможность ввода
# изначальной ссылки и короткого названия и получения изначальной ссылки по её названию.
stuff_file = {'Ivanov': 'Ivan Ivanov, manager', 'Petrov': 'Petro Petrov, accountant',
              'Sidorov': 'Sydir Sidorov, CEO', 'Datikova': 'Maria Datikova, assistant'}

surname = input('Enter a surname of person you need to get info: ').title()
default = f'{surname}: no such person'
print(f'{stuff_file.get(surname, default)}')
