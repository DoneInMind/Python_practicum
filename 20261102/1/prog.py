def fib(m, n):
    a, b = 1, 1
    for x in range(m):
        a, b = b, a + b
    for x in range(n):
        yield a
        a, b = b, a + b

import sys
exec(sys.stdin.read())
