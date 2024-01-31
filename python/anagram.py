s = str(input())
t = str(input())

for i in s:
    if i in t:
        x = t.index(i)
        t = t[0:x]+t[x+1:len(t)]
        
if len(t)>0:
    print("false")
else:
    print("true")

# OR 
lst = []
if len(s) != len(t):
    print("False")
for idx in s:
    if s.count(idx) != t.count(idx):
        lst.append(1)
    else:
        lst.append(0)
if 1 in lst:
    print("False")
else:
    print("True")

