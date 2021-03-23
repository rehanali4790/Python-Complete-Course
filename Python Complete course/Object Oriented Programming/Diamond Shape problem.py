class A:
    def met(self):
        print("Im in class A")

class B(A):
    def met(self):
        print("Im in class B")


class C(A):
    def met(self):
        print("Im in class C")


class D(B,C):
    pass


a = A()
b = B()
c = C()
d = D()
d.met()