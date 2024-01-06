x = int(input("enter your first number: "))
y = int(input("enter your second number: "))
z = input("enter operator: ")

if z == "+"  :
    print("your answer is ",x+y)
elif z =="-":
    print("your answer is ",x-y)
elif z =="x":
    print("your answer is ",x*y)
elif z == "/":
    print("your answer is ",x/y)
else:
    print("enter correct operator")


