# SWAP CASE we need to write a program to swap cases in a string which means lower case to upper case and upper to lower
s = 'aAbBcC'
def swap_case(s):
    l=[]
    str1 = ""
    for i in s :
        if i.islower():
            i = i.upper()
        else:
            i = i.lower()
        l.append(i)
    print(str1.join(l))

swap_case(s)
