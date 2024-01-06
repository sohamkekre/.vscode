res=[-2,1,-3,4,-1,2,1,-5,4]
print(res,len(res))
list=[*set(res)]
print(list,len(list))

list2=[]

for i in range(0,4):
    
     list2.append(list.pop(list.index(max(list))))

print(list2)
print("sum of popped elements",sum(list2))
print(list)
#res=[*set(list)]
#print(res,len(res))



# n=int(input("enter the number of elements in list: "))
# list1=[]
# for i in range(0,n):
#     x=int(input("enter the elements: "))
#     list1.append(x)
# if len(list1)<4:
#     print("run the program again to enter more that 4 numbers!!!")
# else:
#     for i in range (0,4):
#         list2=[list1.pop(list1.index(max(list1)))]
#         print("this is the list of popped elements ",list2)
    
# print(list2)
# class solution:
#     def maxSubArray(self,nums: List[int])->int:
#         max_sum,cur_sum=float('inf'),0
#         for n in nums:
#             cur_sum=max(cur_sum+n,n)
    



