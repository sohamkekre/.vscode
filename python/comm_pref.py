strs = ["flower","flow","flight"]

res =""

for i in range (len(strs[0])):
    for s in strs:
        print(s[i-2])