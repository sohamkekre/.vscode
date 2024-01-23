n = int(input())

def Prime(n):
    if n == 1:
        print("Number is not a prime number")
    elif n > 1:
        for i in range(2,n):
            if n % i == 0:
                return (print("Number is not a prime number"))
        return(print("Yes the number is prime number"))
                

Prime(n)