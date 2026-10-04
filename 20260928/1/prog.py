m, n = eval(input())
primes = [x for x in range(max(2, m), n) if (all(x % y for y in range(2, int(x**0.5) + 1)))]
print(primes)
