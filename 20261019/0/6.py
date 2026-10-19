f = input()
a, b = eval(input())

x, y = a, b
print(eval(f))
x, y = b, a
print(eval(f))
