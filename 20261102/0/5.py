from itertools import dropwhile, islice

def partial_sum():
    s, i = 0, 1
    while True:
        s += 1 / i**2
        yield s
        i += 1

print(*islice(dropwhile(lambda x: x <= 1.6, partial_sum()), 10))
