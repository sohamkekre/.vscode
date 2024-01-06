stack=[]
bracket_map={
    "}" : "{" , ")" : "(" , "]" : "["
}

opening_bracket=set(["(","[","{"])
for x in s:
    if x in opening_bracket:
        stack.append(x)
    elif stack and stack[-1] == bracket_map[x]:
        stack.pop()
    else:
        print("False")
            
if stack:
    print("Flase") 
else:
    print("True")