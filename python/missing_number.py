from jovian.pythondsa import evaluate_test_case,evaluate_test_cases
tests = []
tests.append({
    'input': {
        'num':[3,0,1]
    },
    'output': 2
})
tests.append({
    'input': {
        'num':[-1,-3,-4,-5]
    },
    'output': -2
})
tests.append({
    'input': {
        'num':[9,6,4,2,3,5,7,0,1]
    },
    'output': 8
})

def missing_number(num):
    num = sorted(num)
    for i in num:
        if i != -1:
            if i+1 in num:
                pass
            else:
                return (i+1)
        else:
            if i-1 in num:
                pass
            else:
                return (i-1)

evaluate_test_cases(missing_number,tests)

# Binary Search

# def missing_number(num):
#     num = sorted(num)
#     print(num)
#     mid = len(num)//2
#     mid_number = num[mid]
#     diffrence_left = num[mid] - num[mid-1]
#     diffrence_right = num[mid+1] - num[mid]
#     if diffrence_left > 1:
#         print("left")
#     if diffrence_right > 1:
#         print(num[mid]+1,mid)
#         num.insert(mid+1,num[mid]+1)
#         print(num)
#     else:
#         print(num[mid]-1,mid)
#         num.insert(mid,num[mid]-1)
#         print(num)

# missing_number([9,6,4,2,3,5,7,0,1])
