# Find the sum of Fibonacci even numbers under 4 millions.

fub_1 = 1
fub_2 = 1
sum_even = 0

while (fub_1 + fub_2) < 4000000:
    fub_3 = fub_1 + fub_2

    if fub_3 % 2 == 0:
        sum_even += fub_3
    fub_1, fub_2 = fub_2, fub_3

print(f'The sum of even Fibonacci numbers is {sum_even}')
