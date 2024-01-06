from array import *

arr = array('i',[])
n = int(input("enter the size of array"))

for i in range(0,n):
    x = int(input("enter the values in array"))
    arr.append(x)

print(arr)
# creating array using numpy and also taking user input
# import numpy
# from numpy import *

# arr = array([],dtype=int)
# n = int(input("please enter the length of array"))

# for i in range(0,n):
#     x = int(input("enter the values"))
#     # arr = arr.append(x)
#     arr = numpy.append(arr,x)

# print(arr)
