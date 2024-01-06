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
print(tests)

def locate_card(cards, query):
    # Create a variable position with the value 0
    position = 0
    
    # Set up a loop for repetition
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1

# result = locate_card(test['input']['cards']==test['output']), test['input']['query']) can be written as result = (**test['input']) == test['output'])
# print(result)
# evaluate_test_case(locate_card,test)
evaluate_test_cases(locate_card,tests)
