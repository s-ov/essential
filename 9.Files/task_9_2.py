# Модифицируйте исходный код сервиса по сокращению ссылок из предыдущих двух уроков так, чтобы он сохранял базу ссылок
# на диске и не «забывал» при перезапуске. При желании можете ознакомиться с модулем shelve (https://
# docs.python.org/3/library/shelve.html), который в данном случае будет весьма удобен и упростит выполнение задания.
stuff_file = {'Ivanov': 'Ivan Ivanov, manager', 'Petrov': 'Petro Petrov, accountant',
              'Smirnov': 'Sydir Smirnov, CEO', 'Smith': 'Maria Smith, assistant'}

if __name__ == '__main__':
    surname = input('Enter a surname of person you need to get info: ').title()
    default = f'{surname}: no such person'

    with open('staff_list.txt', 'a') as file:
        file.write(f"Surname: {surname}; Info: {stuff_file.get(surname, default)}\n")

    with open('staff_list.txt') as file:
        for line in file:
            print(line)
