# MRO


class A:
    pass


class B(A):
    pass


class D(A, B):
    pass


print(D())
