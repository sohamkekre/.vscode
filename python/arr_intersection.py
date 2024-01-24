arr1 = list(map(int,input("Enter elements of first arr ").split(" ")))
arr2 = list(map(int,input("Enter elements of second arr ").split(" ")))

intersection = []
for i in arr1:
    if i in arr2:
        intersection.append(i)

print(intersection)