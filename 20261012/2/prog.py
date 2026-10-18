from math import *

W, H, A, B, F = input().split(maxsplit=4)
W, H, A, B = int(W), int(H), eval(A), eval(B)

ys = [eval(F, globals(), {"x": A + i * (B - A) / (W - 1)}) for i in range(W)]

ymin, ymax = min(ys), max(ys)
rows = [round((y - ymin) / (ymax - ymin) * (H - 1)) if ymax > ymin else 0 for y in ys]

screen = [[" "] * W for _ in range(H)]
for i, r in enumerate(rows):
    prev = rows[i - 1] if i else r
    for k in range(min(r, prev + 1), max(r, prev - 1) + 1):
        screen[k][i] = "*"

for line in reversed(screen):
    print("".join(line).rstrip())
