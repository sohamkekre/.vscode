nums = list(map(int,input().split(" ")))
k = int(input())

dict = {}
final = []

for i in nums:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
# print(dict)
keys = list(dict.keys())
values = list(dict.values())
while k > 0:
    max_value = max(values)
    ind = values.index(max_value)
    final.append(keys[ind])
    values.pop(ind)
    keys.pop(ind)
    k -= 1
print(final)
