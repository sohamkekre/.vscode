nums = list(map(int,input().split(" ")))

target = int(input())

i = 0
j = 1

for j in range(len(nums)):
    while i < j:
        if nums[i] + nums[j] == target:
            print(f"[{nums[i]}],[{nums[j]}]")
    i += 1
    
    