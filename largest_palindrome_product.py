def is_palindrome(n):
    n = str(n)
    if n != n[-1::-1]:
        return False
    return True


largest_palindrome = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if is_palindrome(product) and largest_palindrome < product:
            largest_palindrome = product

print(largest_palindrome)
