n = int(input())

def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return (n*factorial(n-1))
    
x = int(input("enter a number: "))
x= factorial(x)
print(x)

# OR

factorial = 1
for i in range (n,0,-1):
    factorial = factorial*i
    print(factorial)