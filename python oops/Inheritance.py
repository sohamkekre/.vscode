class A:
    def __init__(self) -> None:
        print("This is constructor of class A")
    def feature1(self):
        print("This is a feature of class A")

class B(A):
    def feature2(self):
        print("This is a feature of class B")


class C(A):
    def __init__(self) -> None:
        print("This is constructor of class C")

a1 = A()
a2 = B()
a3 = C()
