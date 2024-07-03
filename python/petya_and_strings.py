def petya_and_strings():
    str1 = str(input().lower())
    str2 = str(input().lower())
    i = len(str1)-1
    x = 0
    while i >= 0:
        if str1[i] == str2[i]:
            i -= 1
            continue
        else:
            if ord(str1[i]) < ord(str2[i]):
                x = -1
                i -= 1
            elif ord(str1[i]) > ord(str2[i]):
                x = 1
                i -= 1
            elif ord(str1[i]) == ord(str2[i]):
                x = 0
                i -= 1
    return x

print(petya_and_strings())