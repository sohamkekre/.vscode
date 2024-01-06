n = int(input())
w=len(str(bin(n))[2:])
for i in range (1,n+1):
    print(str(i).rjust(w,' '),oct(i).replace("0o","").rjust(w,' '),hex(i).replace("0x","").upper().rjust(w,' '),bin(i).replace("0b","").rjust(w,' '))
    # print("Octal : ",oct(i).replace("0o",""))
    # print("Hexadecimal : ",hex(i).replace("0x",""))
    # print("Binary : ",bin(i).replace("0b",""))