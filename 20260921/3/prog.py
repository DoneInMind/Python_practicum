n = int(input())

i = n
while (i <= n + 2):
    j = n
    while (j <= n + 2):
        digit_sum = 0
        t = i * j
        while (t > 0):
            digit_sum += t % 10
            t //= 10

        if (j > n):
            print(" ", end = "")
        print(i, "*", j, "=", end = " ")
        if (digit_sum == 6):
            print(":=)", end = "")
        else: print(i * j, end = "")
        j += 1
    print()
    i += 1
