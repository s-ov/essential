# Даны две строки. Выведите на экран символы, которые есть в обоих строках.
string_1 = 'Holland'
string_2 = 'Ireland'
print(f'Common characters: {set(string_1) & set(string_2)}')
