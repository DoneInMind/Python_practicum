x, y = eval(input())
l = len(bin(y)) - 2
for x in range(x, y + 1):
    print(f"{bin(x): <20} = {hex(x)}")
