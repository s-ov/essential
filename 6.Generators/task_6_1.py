def gen_reversed_list(list_):
    for item in list_[::-1]:
        yield item


some_list = [el + 5 for el in range(10, 31, 5)]
print(f'Original list: {some_list}\n')
list_1 = []
gen = gen_reversed_list(some_list)
while True:
    try:
        list_1.append(next(gen))
    except StopIteration:
        break
print(f"Reversed list: [{', '.join(map(str, list_1))}]")
