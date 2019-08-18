import math
import time


def divisor_seq(number):
    max_divisor = math.floor(math.sqrt(number))
    counter = 0
    if max_divisor == math.sqrt(number):
        counter += 1
    for i in range(1, max_divisor + 1):
        if number % i == 0:
            counter += 2
    return counter


start = time.time()
item = 0
while True:

    triangular_number = int(item * (item + 1) / 2)
    if divisor_seq(triangular_number) >= 500:
        break
    item += 1
end = time.time()
print(
    f"Triangular number {triangular_number}, has {divisor_seq(triangular_number)} divisors.\n It takes {end - start} s")
