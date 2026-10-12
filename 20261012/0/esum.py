from fractions import Fraction as F
from decimal import Decimal, getcontext as D

def esum(N, one):
    res = one
    factorial = one
    for i in range(1, N + 1):
        factorial = factorial / type(one)(i)
        res += factorial
    return res

print(esum(20, D(1)))
