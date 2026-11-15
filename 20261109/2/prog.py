class Triangle:
    @staticmethod
    def vector_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    
    def __init__(self, a, b, c):
        a, b, c = map(tuple, (a, b, c))
        if (self.vector_product(a, b, c) < 0): b, c = c, b
        self.p = a, b, c
        self.edges = (a, b), (b, c), (c, a)

    def __abs__(self):
        s = self.vector_product(*self.p)
        return s / 2 if s else 0
    
    def __bool__(self):
        return self.vector_product(*self.p) != 0
    
    def __lt__(self, other):
        return abs(self) < abs(other)
    
    def has_point(self, q):
        return all(self.vector_product(a, b, q) >= 0 for a, b in self.edges)
    
    def separates(self, other):
        return any(all(self.vector_product(a, b, q) < 0 for q in other.p) for a, b in self.edges)
    
    def __contains__(self, other):
        return not other or bool(self) and all(map(self.has_point, other.p))
    
    def __and__(self, other):
        return bool(self) and bool(other) and not (self.separates(other) or other.separates(self))

import sys
exec(sys.stdin.read())
