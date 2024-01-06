def running_sum(nums):
    sum_nums = []
    len_nums = len(nums)
    sum = 0
    for i in range (len_nums):
        if i == 0:
            sum_nums.append(nums[i])
        else:
            sum = nums[i] + sum_nums[i-1]
            sum_nums.append(sum)
    print(sum_nums)

running_sum([1,1,1,1,1])