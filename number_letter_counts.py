import inflect


def lengths(number_string):
    count = 0
    for letter in number_string:
        if letter.isalpha():
            count += 1
    return count


p = inflect.engine()

length = 0

for i in range(1, 1001):
    string = p.number_to_words(i)
    length += lengths(string)
print(length)
