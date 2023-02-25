def input_data(arg1, arg2, arg3):
    with open('staff.txt', "a") as f:
        f.write(f"Surname: {arg1}; Age: {arg2}; Department: {arg3}\n")
    return f


def output_data():
    try:
        with open('staff.txt', "r") as f:
            for line in f:
                print(f"{line}")
    except FileNotFoundError:
        print("File doesn't exist.")


while True:
    option = input("Menu:\nto enter data press '1',\nto output data press '2',\nto exit press '3': ")
    if option == '1':
        surname = input("Enter surname: ").title()
        age = input("Enter age: ")
        department = input("Enter department: ")
        input_data(surname, age, department)
    elif option == '2':
        output_data()
    elif option == '3':
        break
    else:
        print("Incorrect input.")
