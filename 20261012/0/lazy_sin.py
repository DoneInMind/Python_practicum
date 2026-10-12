from math import sin

def scale(a, b, A, B, x):
    return A + (x - a) * (B - A)/(b - a)

W, H, A, B = eval(input())

res = [[' '] * W for x in range(H)]

for i in range(H):
    if (H == 1): x = W-1
    else: x = round(scale(0, W-1, A, B, i))

    y = sin(x)

    if (W == 1): j = H-1
    else: j = round(scale(-1, 1, 0, H-1, y))

    res[j][x] = '*'

for x in res:
    print(*x)
