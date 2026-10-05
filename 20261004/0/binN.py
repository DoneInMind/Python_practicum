
def binN(ones, n, num):
    if (n == 0):
        if (ones == 0): print(num)
        return
    if (ones > 0):
        binN(ones - 1, n - 1, num*2 + 1) 
    
    binN(ones, n - 1, num*2)


n, ones = eval(input())
binN(ones, n, 0)
