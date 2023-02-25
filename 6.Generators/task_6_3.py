def get_n_primes(num):
    prime = 2
    while num > 0:
        for item in range(2, prime):
            if prime % item == 0:
                break
        else:
            yield prime
            num -= 1
        prime += 1


gen = get_n_primes(35)
print(f'First 35 prime numbers:\n{list(gen)}')
