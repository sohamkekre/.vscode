nums = list(map(int,input().split(" ")))

target = int(input())
nums_dict = {}
for i,num in enumerate(nums):
    nums_dict[i] = num

for n in nums:
    subt=target - n 
    if subt in nums_dict.values():
        print(nums_dict.keys[n],nums_dict.keys[subt])

# correction needed as we cannot print the key of a value in the nums_dict        