nums = list(map(int,input().split(" ")))
k = int(input())

def k_frequent(nums,k):
    dict = {}
    lst = []
    for n in nums:
        if n not in dict.keys():
            dict[n] = 1
        else:
            dict[n] += 1

    keys = list(dict.keys())
    values = list(dict.values())
    print(dict)
    

k_frequent(nums,k)