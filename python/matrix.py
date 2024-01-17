import numpy as np

n = int(input())
lst_str = ""
for i in range(n):
    s = str(input())
    lst_str = lst_str + s + " "
    s = ""

lst = []
lst_str = lst_str.split(" ")
for ele in lst_str :
    if ele!='':
        lst.append(int(ele))

lst =np.array()
# print(lst)
# arr = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if i<j:
#             arr[i][j] = 0

# print(arr)