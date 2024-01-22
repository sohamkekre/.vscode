class student:
    def __init__(self,marks) -> None:
        self.marks = marks

    def __add__(self,other):
        m = self.marks + other.marks
        return m
    
s1 = student(50)
s2 = student(50)

s3 = s1 + s2
print(s3)

