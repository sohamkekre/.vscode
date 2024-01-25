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

if len(s) != len(t):
    print("True")
for idx in s:
    if s.count(idx) != t.count(idx):
        print("False")
    else:
        print("True")

