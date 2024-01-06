string = 'aabb'

ans = ""

ans = string[0]

for i in range(1,len(string)):
    if string[i-1] != string[i]:
        ans += string[i]
    
print(ans)