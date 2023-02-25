# Напишите итератор, который возвращает элементы заданного списка в обратном порядке (аналог reversed).

my_list = ["One", "piece", "per", "time", "!"]
new_list = []

for item in range(len(my_list)):
    new_list.append(my_list.pop())
print(new_list)
