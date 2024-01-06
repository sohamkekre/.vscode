s='rat'
t='car'

if len(s) != len(t):
    print("True")
for idx in s:
    if s.count(idx) != t.count(idx):
        print("False")
    else:
        print("True")
