def MinF(*args):
    for y in args:
        for g in args:
            if all((y(x) <= g(x)) for x in range(100)):
                return y

def y1(x): return 4*x + 1
def y2(x): return 5*x + 2
def y3(x): return 7*x + 22
x = int(input())
print(MinF(y1, y2, y3)(x))
