def fun(a, b):
    if isinstance(a, (list, tuple)):
        return type(a)(x for x in a if x not in b)
    return a - b


a, b = eval(input())
print(fun(a, b))
