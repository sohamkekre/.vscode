class student():
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self,other):
        a = self.m1 + other.m1
        b = self.m2 + other.m2
        s3 = student(a,b)
        return s3
    

s1 = student(58,69)
s2 = student(60,65)

s3 = s1+s2
print(s3.m1)
        