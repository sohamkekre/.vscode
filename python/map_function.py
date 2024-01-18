n = int(input())
s = str(input())
s = s.split(" ")
lst = []
for i in s:
    lst.append(int(i))
    
print(lst)
def square(i):
    return (i*i)

sqr_lst = tuple(map(square,lst))

print(sqr_lst)

