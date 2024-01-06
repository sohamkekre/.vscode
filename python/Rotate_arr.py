def inp_to_otp (k,s):
    s = s.split(' ')
    arr = []
    for i in s:
        x = int(i)
        arr.append(x)
    return arr,k

k = int(input("Number of time of rotation "))
s = str(input("Enter the array "))
arr,k = inp_to_otp(k,s)


def rotate(arr,k):
    copy = arr.copy()
    i = 0
    length = len(arr)-1
    while i <= length:
        x = arr[i]
        j = i+k
        if j > length:
            j = j - length - 1
            copy[j] = x
        else:
            copy[j] = x
        i = i+1
    return (print(copy))

rotate(arr,k)