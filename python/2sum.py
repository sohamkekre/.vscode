nums = list(map(int,input().split(" ")))

target = int(input())

def two_sum(nums,target):
    nums_dict = {}
    for i,num in enumerate(nums):
        nums_dict[i] = num

    for n in nums:
        subt=target - n 
        if subt in nums_dict.values():
            for key , value in nums_dict.items():
                if subt == value:
                    if nums.index(n) == key:
                        pass
                    else:
                        return(print(nums.index(n),key))

two_sum(nums,target)

# second solution function.

def twosum(nums,target):
    complimentMap = dict()
    for i in range(len(nums)):
        num = nums[i] #2
        compliment = target - num #7
        if num in complimentMap:
            print( [complimentMap[num], i]) #in second iteration it will print the index which is stored in dic(compliment) and will also print the present value of i
        else:
            complimentMap[compliment]=i #{7,0} 

twosum(nums,target)
