n = int(input())
reslist = []
for i in range (n):
    command = input().split()
    if command[0] == 'insert':
        reslist.insert(int(command[1]),int(command[2]))
    elif command[0] == 'print':
        print(reslist)
    elif command[0] == 'remove':
        reslist.remove(int(command[1]))
    elif command[0] == 'append':
        reslist.append(int(command[1]))
    elif command[0] == 'sort':
        reslist.sort()
    elif command[0] == 'pop':
        reslist.pop()
    elif command[0] == 'reverse':
        reslist.reverse()
    