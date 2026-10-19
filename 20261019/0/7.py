from collections import Counter

a, b = input(), input()
A = Counter(a.split())
B = Counter(b.split())

res = True
for w, cnt in B.items():
    if (A.get(w) == None or A.get(w) < cnt): res = False

print(res)
