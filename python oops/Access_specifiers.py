class A:
    def __init__(self,name,age,rollno) -> None:
        self.name = name        #public
        self._age = age         #protected
        self.__rollno = rollno  #private
    def __display(self):                  #private method
        print(f"The name of student is {self.name}, his age is {self._age}, and his role number is {self.__rollno}.")
    def _display_protected(self):         #protected method
        print(f"This is a protected class")
    def display_private_data(self):       #public method
        self.__display()

class B(A):
    pass

a1 = A("a",26,1)
b1 = B("b",1,25)
# a1._display_protected()
# print(a1.__rollno)
# print(a1._age)