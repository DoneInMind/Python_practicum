class Rectangle:
    x1, x2, y1, y2 = 0, 0, 0, 0
    points = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
    rectcnt = 0
    def __init__(self, x1, x2, y1, y2):
        """self.__setattr__(self, f"rect_<{str(self.__class__.rectcnt + 1)}>", self.__class__.rectcnt + 1)"""
        self.__class__.rectcnt += 1
        self.x1, self.x2, self.y1, self.y2 = x1, x2, y1, y2
        self.points = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
    def __str__(self):
        print(f"(({self.x1}, {self.y1}), ({self.x1}, {self.y2}), ({self.x2}, {self.y1}), ({self.x2}, {self.y2}))")
        print(f"Количество объектов класса равно {self.__class__.rectcnt}")
    def __abs__(self):
        return (abs(self.x2 - self.x1) * abs(self.y2 - self.y1))
    def __lt__(self, other):
        return (abs(self) < abs(other))
    def __eq__(self, other):
        return (abs(self) == abs(other))
    def __bool__(self):
        return (abs(self) != 0)
    def __mul__(self, k):
        self.x1 *= k; self.x2 *= k; self.y1 *= k; self.y2 *= k
        self.points = [(self.x1, self.y1), (self.x1, self.y2), (self.x2, self.y1), (self.x2, self.y2)]
    __rmul__ = __mul__

    def __getitem__(self, idx):
        return self.points[idx]
    def __iter__(self):
        return (iter(self.points))
    
    def __del__(self):
        self.__class__.rectcnt -= 1
        print(self.__class__.rectcnt)

a = Rectangle(1, 2, 3, 4)
a.__mul__(6)
for x, y in a:
    print(x, y)
