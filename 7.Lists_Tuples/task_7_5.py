# Напишите программу, которая вводит с клавиатуры последовательность чисел и выводит её отсортированной
# в порядке возрастания.
def ascend_numbers(arg):
    return ' '.join(map(str, sorted(arg)))


if __name__ == '__main__':
    try:
        list_of_numbers = list(map(int, input('Enter arbitrary range of numbers separated with space: ').split(' ')))
    except ValueError:
        list_of_numbers = []
        print("InputError: numbers must be separated with one space.")
    print(f'Original range of numbers: {list(list_of_numbers)}')
    print(f'Sorted range of numbers: {ascend_numbers(list_of_numbers)}')
