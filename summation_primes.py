import math
import time


def is_prime(n):
    if n == 1:
        return False

    if n == 2:
        return True

    if n > 2 and n % 2 == 0:
        return False
    max_divisor = int(math.floor(math.sqrt(n)))

    for i in range(3, max_divisor + 1, 2):
        if n % i == 0:
            return False
    return True


def prime_generator(bond):
    for i in range(1, bond + 1):
        if is_prime(i):
            yield i


start = time.time()
two_million_primes = prime_generator(2000000)
print(sum(two_million_primes))
end = time.time()
print(f"It takes {end - start} s")
