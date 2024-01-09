def inp_to_otp (k,s):
    s = s.split(' ')
    arr = []
    for i in s:
        x = int(i)
        arr.append(x)
    return arr,k

k = int(input("Number of elements in array "))
s = str(input("Enter the array "))
arr,k = inp_to_otp(k,s)
