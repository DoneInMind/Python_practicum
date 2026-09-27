s = 0
while (s <= 21):
    x = int(input())
    if (x <= 0):
        print(x)
        break
    s += x
else:
    print(s)
