import numpy as np

#a=np.array([1,2,3,4,5,6,7])
n=int(input("how many array inputs: "))
a=[]
for i in range(0,n):
    x=int(input())
    a.append(x)

max=a[0]
min=a[0]

for i in range(1,len(a)):
    if a[i]>max:
        max=a[i]
    elif a[i]<min:
        min=a[i]

print(f"Max={max} and Min={min}")