nums = dict(map(int,input().split(" ")))
print(nums)

target = int(input())

for n in nums:
    subt = target - n
    if subt in nums:
        if nums.index(n) != nums.index(subt):
            print(f"[{nums.index(n)},{nums.index(subt)}]")
            break
    else:
        continue

# still correction needed with same elements in an array
    



    