from fractions import Fraction as F
from decimal import Decimal as D

def multiplier(x, y, type):
    return type(x) * type(y)

print(multiplier("1/6", "2/3", F))
