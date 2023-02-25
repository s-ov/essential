list_1 = [item ** 5 for item in range(5, 26)]
print(f'{list_1}\n')

gen = (i ** 5 for i in range(5, 26))
list_2 = []
while True:
    try:
        list_2.append(next(gen))
    except StopIteration:
        break
print(', '.join(map(str, list_2)))
