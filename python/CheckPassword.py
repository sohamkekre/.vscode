def CheckPassword(str,n):
    flag_list = []
    if str[0].isnumeric() and n<4:
        return flag_list.append(0)
    else :
        flag_list.append(1)
    
        for element in str:
            if element.isnumeric():
                flag_list.append(1)
            elif element.isupper():
                flag_list.append(1)
            elif element == " " or element == "/":
                flag_list.append(0)
    if 0 in flag_list:
        print("0")
    else:
        print("1")
CheckPassword("aA1_67",6)