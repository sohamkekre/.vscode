class student:
    def sum(self,a = None,b = None,c = None):
        sum = 0
        if (a and b and c!=None):
            sum = a+b+c
            print(sum)
        elif(a and b!=None):
            sum=a+b
            print(sum)
        else:
            sum = a
            print(sum)
    
s1 = student()
s1.sum(5)