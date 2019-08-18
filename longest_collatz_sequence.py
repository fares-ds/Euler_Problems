# A Solution that takes about 1.1 seconds in python
def main():
    known = {1: 1}
    max_count = 0
    start_num = 0
    for i in range(1, 1000000):
        count = 0
        num = i
        while True:
            count += 1
            if num in known:
                count += known[num] - 1
                break
            if num % 2 == 0:
                num = num // 2
            else:
                num = 3 * num + 1
        known.setdefault(i, count)
        if count > max_count:
            start_num = i
            max_count = count

    print(f'Max count is {max_count} at {start_num}')


main()
