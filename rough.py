k = int(input("Number of elements in array "))
s = str(input("Enter the array "))

def inp_to_otp (k,s):
    arr = list(map(int,s.split(" ")))
    return arr,k

def inp_to_otp2(k,s):
    s = s.split(' ')
    arr = []
    for i in s:
        x = int(i)
        arr.append(x)
    return arr,k

# arr,k = inp_to_otp(k,s)
# print(arr,k)
# arr,k = inp_to_otp2(k,s)
