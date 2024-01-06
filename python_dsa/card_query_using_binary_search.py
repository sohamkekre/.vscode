from jovian.pythondsa import evaluate_test_case
from jovian.pythondsa import evaluate_test_cases

test = {
    'input': { 
        'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
        'query': 7
    },
    'output': 3
}            
tests = []        
tests.append(test)

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

def  locate_cards(cards,query):
    lo,hi = 0,len(cards)-1

    while lo <= hi:
            mid = (lo + hi)//2
            mid_number = cards[mid]
            if mid_number == query:
                  return mid
            elif mid_number < query:
                  hi = mid - 1
            elif mid_number > query:
                  lo = mid + 1
    return -1

evaluate_test_cases(locate_cards,tests)