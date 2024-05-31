nums = list(map(int,input("Enter the elements of the array: ").split(" ")))
# print(nums)
def Product_of_self_except_self(nums):
    final = []
    for i in nums:
        left_prod = 1
        right_prod = 1
        idx = nums.index(i)
        for j in range(0,idx):
            left_prod = left_prod * nums[j]
        for k in range(idx+1,len(nums)):
            right_prod = right_prod * nums[k]
        prod = left_prod * right_prod
        final.append(prod)

    return(final)
print(Product_of_self_except_self(nums))
