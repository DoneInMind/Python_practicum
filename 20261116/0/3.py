def _init(self, x = 0):
    setattr(self, "val", x)
def _str(self):
    print(f"{self.val}")

C = type("C", (), {"foo": lambda self, n: self.val * n, "__init__": _init, "__str__": _str})

c = C()
b = C(7)
print(c.val)
print(c.foo(3))
print(b.val)
print(b.foo(3))
