def closure(a, b):
    def y(x, a = a, b = b):
        return a * x + b
    return y

print(closure(1, 2)(4))
print(closure(2, 3)(4))
