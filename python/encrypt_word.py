def encrypt_word(n,s,k):
    str1 = 'ABCDEFGHIJKLMNOPQRSTUWXYZ'
    str = 'abcdefghijklmnopqrstuwxyz'
    
    for i in s:
        if i in str or i in str1:
            if i == i.lower():
                x = str.index(i)
                if (x + k) <25:
                    s = s.replace(i,str[x+k])
                elif (x + k) >= 25:
                    j = (x + k) - 25
                    s = s.replace(i,str[j])
            else:
                x = str1.index(i)
                if (x + k) <25:
                    s = s.replace(i,str1[x+k])
                elif (x + k) >= 25:
                    j = (x + k) - 25
                    s = s.replace(i,str1[j])  
        else:
            continue          
    print(s)
    
encrypt_word(11,'middle-Outz',2)
