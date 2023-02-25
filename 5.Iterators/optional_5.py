from itertools import cycle


def infinite(lst, iterations):
    result = ''
    iter_lst = cycle(lst)
    if lst:
        for symbol in range(iterations):
            result += str(next(iter_lst))
    return result
# Тесты
# print(infinite([2, 5, 8, 13, 21, 45, 145, 210, 233], 7))
# print(infinite(['/', r'\''], 70))
# print(infinite([], 1000))
# print(infinite([7], 4))
l = [1,1,2,3,8]
print(l)
a = list(range(len(l)))
print(a)
