def helpful_maths():
    inpt = list(map(int,input().split("+")))
    inpt.sort()
    summands = ""
    for i in inpt:
        s = str(i)
        summands = summands + f"+{s}"
    return summands[1:]
print(helpful_maths())