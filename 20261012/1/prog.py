from fractions import Fraction as F

def check(a, b, s, w):
    s, w = F(s), F(w)

    B = F(0)
    for x in b:
        B = B * s + F(x)

    if (B == 0): return False

    A = F(0)
    for x in a:
        A = A * s + F(x)

    return A == w * B


data = input().replace(',', ' ').split()

s = F(data[0])
w = F(data[1])

deg_a = int(data[2])
a = list(map(F, data[3 : 3 + deg_a + 1]))

pos = 3 + deg_a + 1
deg_b = int(data[4 + deg_a])
b = list(map(F, data[5 + deg_a : 6 + deg_a + deg_b]))

print(check(a, b, s, w))
