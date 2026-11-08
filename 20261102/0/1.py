def partial_sum():
    s, i = 0, 1
    while True:
        s += 1 / i**2
        yield s
        i += 1
