lines = []
while (s := input().strip()) != "":
    lines.append([int(x) for x in s.split(',')])

n = len(lines) // 2
res = [[0] * n for x in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            res[i][j] += lines[i][k] * lines[n + k][j]

for i in range(n):
    print(','.join(map(str, res[i])))
