strs = list(map(str,input().split(" ")))
# print(strs)

def grp_anagram(strs):
    result = []
    ptr = 0
    i = 1
    while ptr < len(strs) and ptr < i :
        lst = []
        i = ptr + 1
        s = strs[ptr]
        lst.append(s)
        while i < len(strs):
            check_lst = []
            for letter in s:
                if s.count(letter) == strs[i].count(letter):
                    check_lst.append(1)
                else:
                    check_lst.append(0)
            if 0 not in check_lst and check_lst != [] :
                lst.append(strs[i])
                strs.pop(i)
            i += 1
        result.append(lst)
        ptr += 1
    return result

x = grp_anagram(strs)
print(x)

# still correction remaining