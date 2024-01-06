a = input("Enter any value between 5 and 9: ")

if a == 'quit' :
    print("you will be directed on home page")
elif (int(a)>5 and int(a)<9):
    print("you entered correct value")
elif (int(a)<5 or int(a)>9):
    raise ValueError
else:
    raise TypeError