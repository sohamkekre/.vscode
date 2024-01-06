def ReplaceCharacter(str,n,ch1,ch2):
    if ch1 and ch2 in str:
        str = str.replace(ch1,'1')
        str = str.replace(ch2,ch1)
        str = str.replace('1',ch2)
    return(print(str))    

ReplaceCharacter('apples',6,'a','p')