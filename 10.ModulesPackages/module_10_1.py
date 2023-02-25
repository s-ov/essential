from task_10_1 import*

stuff_file = {'Ivanov': 'Ivan Ivanov, manager', 'Petrov': 'Petro Petrov, accountant',
              'Smirnov': 'Sydir Smirnov, CEO', 'Smith': 'Maria Smith, assistant'}

if __name__ == '__main__':
    while True:
        menu = input("Menu:\n1.Print data in to text file.\n"
                     "2.Print in to console.\n3.Add data.\n4.Exit."
                     "Choose 1, 2, 3 or 4: _")

        if menu not in ['1', '2', '3', '4']:
            print(f"'{menu}': no such option in menu.")
            continue
        elif menu == '4':
            print("Program is closed.")
            break

        if menu == '2':
            output_data()
        elif menu == '1':
            surname = input('Enter a surname of person you need to get info: ').title()
            default = f'{surname}: no such person'
            input_data(surname, stuff_file.get(surname, default))
        elif menu == '3':
            surname = input('Enter a surname of person you need to add to the list: ').title()
            surname_info = input('Enter full name and position of the person: ')
            add_data(stuff_file, surname, surname_info)
