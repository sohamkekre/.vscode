def subArraySum(arr,n,s):
    left = 0
    right = 1
    current_sum = arr[left] +arr[right]
    while right and left < n:
        if current_sum == s:
            print(left+1,right+1)
            break
        elif current_sum < s :
            right = right + 1
            current_sum = current_sum + arr[right]
        elif current_sum > s:
            current_sum = current_sum - arr[left]
            left = left + 1
            if current_sum == s:
                print(left+1,right+1)
                break
            else:
                current_sum = current_sum + arr[left]
        
    

subArraySum([1,2,3,7,5],5,12)