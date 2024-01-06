A=[3,1,2,5,3]

#we have to print the number which appears twice in A
#and also the mssing number in the series
#output here should be [1,3]

ans=[]
Sum1=sum(A)
n=len(A)
s=n*(n+1)//2
A=list(set(A))
Sum2=sum(A)
rep_num=0
if Sum1>Sum2:
    rep_num=Sum1-Sum2

ans.append(rep_num)
ans.append(s-Sum2)
print(ans)