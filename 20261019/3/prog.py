from collections import Counter as C

l = int(input())
s = []
while (line := input()) != "":
    s.append(line)

clean = ''.join(c if c.isalpha() else ' ' for c in ' '.join(s).lower())
cnt = C(x for x in clean.split() if len(x) == l)

if (len(cnt) > 0):
    print(*sorted(w for w, k in cnt.items() if k == max(cnt.values())))
