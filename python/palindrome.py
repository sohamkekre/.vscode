s="A man, a plan, a canal: Panama"

new_s=""

for i in s:
    if i.isalnum():
        new_s += i.lower()

print(new_s)

left=0
right=len(new_s)-1

for i in range(0,right):
    if new_s[left] == new_s[right-1]:
        x=1
    else:
        x=0
        left = left+1
    right = right-1

    print(x)
