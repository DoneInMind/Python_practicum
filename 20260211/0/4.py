def travel(n):
    for x in range(n): yield "По кочкам"
    return "В яму"

def travelwrap(n):
    res = yield from travel(n)
    yield res
