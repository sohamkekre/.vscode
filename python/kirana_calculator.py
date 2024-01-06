sum = 0
while(True):
    userinpt = input("enter the item amount:\n ")
    if userinpt != 'q':
        sum = sum + int(userinpt)
        print(f"your order total till now is {sum}")
    else :
        print(f"your total bill is {sum}. Thanks for using our calculator ")
        break