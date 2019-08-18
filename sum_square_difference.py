def difference(n):
    sum_of_number = sum([i for i in range(1, n + 1)])
    sum_of_squares = sum([i * i for i in range(1, n + 1)])

    return sum_of_number ** 2 - sum_of_squares


print(difference(100))
