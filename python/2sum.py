# nums = [2,7,11,15], target = 9
def twosum(nums,target):
    complimentMap = dict()
    for i in range(len(nums)):
        num = nums[i] #2
        compliment = target - num #7
        if num in complimentMap:
            print( [complimentMap[num], i]) #in second iteration it will print the index which is stored in dic(compliment) and will also print the present value of i
        else:
            complimentMap[compliment]=i #{7,0} 

twosum([2,7,11,15],9)

# for i in range(len(nums)):
    #     for j in range (i+1,len(nums)):
    #         sum = nums[i] + nums[j]
    #         if sum == target :
    #             print([i,j])