import random


def shuffle(lst):
    l = len(lst)

    if l <= 1:
        return lst
    i = 0
    while l > 1:
        p = int(random.random() * l)
        lst[i], lst[i + p] = lst[i + p], lst[i]
        i += 1
        l -= 1
    return lst


print(shuffle([1, 2, 2, 3, 3, 4, 5, 10]))
