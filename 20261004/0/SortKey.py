arr = eval(input())
sortedArr = sorted(arr, key = lambda x: x*x % 100)
print(*sortedArr)
