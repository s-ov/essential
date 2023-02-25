# Создайте модуль для получения простых чисел.
def get_primes(num):
    for i in range(2, num + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i


def get_n_primes(num):
    prime = 2
    while num > 0:
        for i in range(2, prime):
            if prime % i == 0:
                break
        else:
            yield prime
            num -= 1
        prime += 1
