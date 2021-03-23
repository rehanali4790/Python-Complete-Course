class A:
    classvar1 = "Iam a class A varible"
    def __init__(self):
        self.var1 = "Iam inside class A variable"
        self.classvar1 = "instance var in A class"
        self.special = "special"
class B(A):
    classvar1 = "Iam a class B varaible"

    def __init__(self):
        super().__init__()
        self.var1 = "Iam inside class B variable"
        self.classvar1 = "instance var in B class"


a = A()
b = B()
print(b.special,b.classvar1,b.var1)
