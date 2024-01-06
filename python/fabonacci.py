# fabonacci series = 0 , 1 , 1 , 2 , 3 , 5 .........
n = int(input())
def fabonacci(n):
    f0=0
    f1=1
    l = [f0,f1]
    if (n == 0):
        print(f0)
    elif(n == 1):
        print(f0,f1)
    else:
        for i in range (n-1):
            f2 = f0 + f1
            l.append(f2)
            f0 = f1
            f1 = f2
    print(l)
fabonacci(n) 