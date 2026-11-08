from itertools import product

print(*map(''.join, product("abcdefg", "12345678")))
