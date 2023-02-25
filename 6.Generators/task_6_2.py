# generator method
evens_squared = [i ** 2 for i in range(1, 21) if i % 2 == 0]
print(f'{evens_squared}\n')

# solution with the help of cycle
even_list = []
for i in range(1, 21):
    if i % 2 == 0:
        even_list.append(i ** 2)
print(even_list)
