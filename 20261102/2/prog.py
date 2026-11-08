from itertools import islice, tee

def slide(seq, n):
    end = object()
    while True:
        seq, window = tee(seq)
        yield from islice(window, n)
        if (next(seq, end) is end): return

import sys
exec(sys.stdin.read())
