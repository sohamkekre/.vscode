# Rotated List
from jovian.pythondsa import evaluate_test_case,evaluate_test_cases
tests = []
test = {
    'input':{
        'nums':[19, 25, 29, 3, 5, 6, 7, 9, 11, 14]   
    },
    'output':3
}
test1 = {
    'input':{
        'nums':[1,2,3,4,5,6]
    },
    'output':0
}
test2 = {
    'input':{
        'nums':[]
    },
    'output':0
}
test3 = {
    'input':{
        'nums':[2,3,4,5,6,1]
    },
    'output':5
}

tests  = [test,test1,test2,test3]

def count_rotation_brute_force(nums):
    if len(nums)>0:
        sorted_nums = sorted(nums)
        x = sorted_nums[0]
        return(nums.index(x))
    else:
        return 0
    
def count_rotation_linear_search(nums):
    position = 0
    while position < len(nums):
        if position > 0 and nums[position] < nums[position-1]:
            return position
        else:
            position +=1
    return 0

def count_rotation_binary_search(nums):
    lo = 0
    hi = len(nums)-1
    while lo <= hi:
        mid = (lo + hi)//2
        mid_number = nums[mid]
        if mid > 0 and mid_number<nums[mid-1]:
            return mid
        elif mid_number<nums[hi]:
            # Answer lies in the left half
            hi = mid - 1  
        else:
            # Answer lies in the right half
            lo = mid + 1
    return 0

evaluate_test_cases(count_rotation_binary_search,tests)
