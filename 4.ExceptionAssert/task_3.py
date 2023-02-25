# Опишите класс сотрудника, который включает в себя такие поля, как имя, фамилия, отдел и год поступления на работу.
# Конструктор должен генерировать исключение, если заданы неправильные данные. Введите список работников с клавиатуры.
# Выведите всех сотрудников, которые были приняты после заданного года.

class Employee(object):
    def __init__(self, first_name, second_name, department_, year_of_employing):
        self.__name = first_name
        self.__surname = second_name
        self.__department = department_
        self.__year = year_of_employing

    def _get_name(self):
        return self.__name

    def _get_surname(self):
        return self.__surname

    def _get_department(self):
        return self.__department

    def _get_year(self):
        return self.__year

    def _set_name(self, new_name):
        if new_name.isalpha():
            self.__name = new_name
        else:
            print("Value error!")
            return 'Empty_field'
        return self.__name

    def _set_surname(self, new_surname):
        if new_surname.isalpha():
            self.__surname = new_surname
        else:
            print("Value error!")
            return 'Empty_field'
        return self.__surname

    def _set_department(self, new_department):
        if new_department.isalpha():
            self.__department = new_department
        else:
            print("Value error!")
            return 'Empty_field'
        return self.__department

    def _set_year(self, another_year):
        if another_year.isnumeric() and len(another_year) == 4:
            self.__year = another_year
        else:
            raise ValueError("Year must have four digits!")
        return self.__year

    def _get_info(self):
        return f"{self._get_name()} {self._get_surname()}: {self._get_department()}, {self._get_year()}"

    def show_info(self):
        return self._get_info()


if __name__ == '__main__':
    default_employee = Employee('empty_field', 'empty_field', 'empty_field', 1900)
    try:
        employees = int(input("Enter a number of employees: "))
    except ValueError:
        raise ValueError("Entered data must be integer.")

    stuff_list = []

    for employee in range(employees):
        name = input("Enter a name of employee: ")
        emp_name = default_employee._set_name(new_name=name.title())
        surname = input("Enter a surname of employee: ")
        emp_surname = default_employee._set_surname(new_surname=surname.title())
        department = input("Enter a department of employee: ")
        emp_department = default_employee._set_department(new_department=department.title())
        year = input("Enter a first year of employee carrier: ")
        emp_year = default_employee._set_year(another_year=year)

        emp_data = Employee(emp_name, emp_surname, emp_department, emp_year)
        stuff_list.append(emp_data)

    for man in stuff_list:
        if True:
            if int(man._get_year()) > 1970:
                print(man.show_info())
        else:
            print("No data.")
