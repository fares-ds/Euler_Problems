# The smallest positive number that is evenly divisible by all of the numbers
# from 1 to 20?
from math import factorial


def find_smallest_multiple(n):

    for i in range(n, factorial(n) + 1, n):
        if is_multiple(i, n):
            return i
    return -1


def is_multiple(x, n):
    for i in range(1, n):
        if x % i != 0:
            return False
    return True


print(find_smallest_multiple(20))
