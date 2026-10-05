def average(*args):
    if (not(args)):
        return 0
    return (sum(args) / len(args))

arr = eval(input())
print(average(*arr))
