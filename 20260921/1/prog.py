x = int(input())

if (x % 25 == 0):
    if (x % 2 == 0):
        print("A + B - ", end = "")
    else: print("A - B + ", end = "")
else:
    print("A - B - ", end = "")

if (x % 8 == 0):
    print("C +")
else: print("C -")
