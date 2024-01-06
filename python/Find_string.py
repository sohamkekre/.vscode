string = str(input())
subs_string = str(input())
sl = len(string)
ssl = len(subs_string)
c=0
for i in range(len(string)):
    if string[i:i+ssl] == subs_string:
        c=c+1
print(c)