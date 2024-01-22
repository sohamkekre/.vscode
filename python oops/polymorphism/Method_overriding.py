class A:
    def display(self):
        print("this is the display of A")

class B(A):
    def display(self):
        print("this is the display of B")

a = B()
a.display()