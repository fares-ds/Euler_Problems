import time

start = time.time()
for a in range(1, 500):
    for b in range(a, 500):
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2:
            print(f"a = {a}, b = {b}, c = {c}")
            break
print(f"It takes {time.time() - start}")
