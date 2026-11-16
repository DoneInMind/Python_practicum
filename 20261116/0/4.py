class A:
    def __str__(self):
        print("A", end = '')

class B(A):
    def __str__(self):
        super().__str__()
        print("B", end = '')

class C(B):
    def __str__(self):
        super().__str__()
        print("C", end = '')

C().__str__()
print()
B().__str__()
print()
A().__str__()
