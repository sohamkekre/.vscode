prices=[7,1,5,3,6,4]

left=0
right=1
max_profit=0

while right < len(prices):
    curr_profit = prices[right] - prices[left]
            
    if prices[left] < prices[right]:
        max_profit = max(curr_profit,max_profit)
    else:
        left = right
    right += 1
                
print(max_profit)