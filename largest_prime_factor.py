import math


#
# def is_prime(n):
#     if n == 1 or n < 0:
#         return False
#
#     if n == 2:
#         return True
#
#     if n > 2 and n % 2 == 0:
#         return False
#     max_divisor = math.floor(math.sqrt(n))
#
#     for i in range(3, max_divisor + 1, 2):
#         if n % i == 0:
#             return False
#     return True
#
#
# def prime_factors(number):
#     product = 1
#     lst_of_prime_factors = []
#
#     for largest_prime in range(1, int(number)):
#         if number % largest_prime == 0 and is_prime(largest_prime):
#             lst_of_prime_factors.append(largest_prime)
#             product *= largest_prime
#             if product == number:
#                 break
#     return lst_of_prime_factors
#


def prime_factors(number):
    max_prime = -1

    while number % 2 == 0:
        max_prime = 2
        number /= 2

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            max_prime = i
            number /= i

    if number > 2:
        max_prime = number

    return int(max_prime)


nbr_1 = 600851475143
nbr_2 = 25698751364526
nbr_3 = 20188888888888

print(f"Biggest Prime factors of {nbr_1} : {prime_factors(nbr_1)}")
print(f"Biggest Prime factors of {nbr_2} : {prime_factors(nbr_2)}")
print(f"Biggest Prime factors of {nbr_3} : {prime_factors(nbr_3)}")
