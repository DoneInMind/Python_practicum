from collections import defaultdict

class Omnibus:
    _d = defaultdict(set)

    def __setattr__(self, name, value):
        self._d[name].add(self)

    def __getattr__(self, name):
        return len(self._d[name])

    def __delattr__(self, name):
        self._d[name].discard(self)

import sys
exec(sys.stdin.read())
