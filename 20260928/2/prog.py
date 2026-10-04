def key(x):
    return (x * x) % 100

def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        cur = arr[i]
        cur_key = key(cur)
        j = i - 1
        while j >= 0 and key(arr[j]) > cur_key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = cur
    return arr

arr = list(map(int, input().strip().split(',')))
print(insertionSort(arr))
