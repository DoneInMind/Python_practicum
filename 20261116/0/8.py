def div(a, b, eps):
    try:
        if (0 < b < eps): raise ZeroDivisionError
    except ZeroDivisionError:
        print("Знаменатель ничтожно мал!")
    else:
        return (a / b)


print(div(100, 2, 0.5))
print(div(100, 2, 3))
