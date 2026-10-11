def Pareto(*pairs):
    res = set()
    max_y = float('-inf')
    for x, y in sorted(pairs, reverse=True):
        if (y > max_y):
            res.add((x, y))
            max_y = y
    return tuple(p for p in pairs if p in res)

pairs = eval(input() + ",")
print(Pareto(*pairs))
