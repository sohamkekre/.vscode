strs = list(map(str,input().split(" ")))

def grp_anagrams(strs):
    dict = {}
    for s in strs:
        w = "".join(sorted(s))
        if w in dict:
            dict[w].append(s)
        else:
            dict[w] = [s]
    return dict.values()
    
print(grp_anagrams(strs))