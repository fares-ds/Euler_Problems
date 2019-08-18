import math


def is_prime(n):
    if n == 1 or n < 0:
        return False

    if n == 2:
        return True

    if n > 2 and n % 2 == 0:
        return False
    max_divisor = math.floor(math.sqrt(n))

    for i in range(3, max_divisor + 1, 2):
        if n % i == 0:
            return False
    return True


def prime_generator(n_th):

    prime_position = 0
    i = 1
    while prime_position != n_th:
        if is_prime(i):
            yield i
            prime_position += 1
        i += 1


x = prime_generator(10001)

x = list(x)
print(x[-1])
