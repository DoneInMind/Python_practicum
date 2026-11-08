from itertools import filterfalse

def ffn(n, seq):
    return filterfalse(lambda x: x % n, seq)

import random
print(list(ffn(5, (random.randrange(50) for i in range(100)))))
