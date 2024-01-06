def ProductSmallestPair(sum, arr):
    x = min(arr)
    arr.pop(arr.index(x))

    y = min(arr)
    arr.pop(arr.index(y))

    if len(arr)<2 or (x + y > sum):
        return (print(-1))
    elif (x + y <= sum):
        return (print(x*y))
    

ProductSmallestPair(4,[9,8,3,-7,3,9])