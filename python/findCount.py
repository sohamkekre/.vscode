def findCount(arr,length,num,diff):
    count = 0
    if length == 0 :
        return (print("-1"))
    for element in arr:
        absolute_difference = abs(element - num)
        if absolute_difference <= diff:
            count += 1
    return (print(count))

findCount([12,3,14,56,77,13],6,13,2)