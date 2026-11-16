from itertools import permutations

class A: pass
class B: pass

class C(A, B): pass
class D(B, A): pass

cnt = 0
valid = []
for x in permutations((A, B, C, D), 2):
    if C not in x: continue

    try:
        E = type("E", x, {})
    except TypeError:
        pass
    else:
        cnt += 1
        valid.append(tuple(cls.__name__ for cls in x))
        
print(cnt)
print(valid)
