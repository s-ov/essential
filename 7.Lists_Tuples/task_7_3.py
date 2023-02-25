# Напишите программу, которая вводит с клавиатуры текст и выводит отсортированные по алфавиту слова данного текста.
def sort_words(words):
    return ' '.join(sorted(words.lower().split(' ')))


if __name__ == '__main__':
    string = input('Enter some text.\n')
    print(sort_words(string))
