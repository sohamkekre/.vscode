def three_sum(nums):
    length = len(nums)
    nums.sort()
    result = []
    for i in range(length - 2):
        if i>0 and nums[i] == nums[i-1]:
            continue
        l = i + 1
        r = length -1

        while l<r:
            total = nums[l] + nums[r] + nums[i]
            if total>0:
                r = r-1
            elif total<0:
                l = l+1
            else:
                result.append([nums[i],nums[l],nums[r]])
                while l<r and nums[l] == nums[l+1]:
                    l = l+1
                while l<r and nums[r] == nums[r-1]:
                    r = r-1
                l = l+1
                r = r-1

    print(result)

three_sum([-1,0,1,2,-1,-4])