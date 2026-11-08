from itertools import repeat

def repeater(a, n):
    for x in a:
        yield from repeat(x, n)
