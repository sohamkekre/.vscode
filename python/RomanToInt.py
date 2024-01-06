# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
from jovian.pythondsa import evaluate_test_case,evaluate_test_cases
tests = []
test = {
    'input':{
        's':'DCXXI'
    },
    'output':621
}
tests.append(test)

def RomanToInt(s):
    dependency = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
    roman_characters = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    sum = 0
    if "IV" in s:
        sum = sum+dependency["IV"]
        s=s.replace("IV","")
    if "IX" in s:
        sum = sum + dependency["IX"]
        s=s.replace("IX","")
    if "XL" in s:
        sum = sum+dependency["XL"]
        s=s.replace("XL","")
    if "XC" in s:
        sum = sum+dependency["XC"]
        s=s.replace("XC","")
    if "CD" in s:
        sum=sum+dependency["CD"]
        s=s.replace("CD","")
    if "CM" in s:
        sum=sum+dependency["CM"]
        s=s.replace("CM","")
    if len(s)>0:
        for n in s:
            x = roman_characters[n]
            sum = sum+x        
    return sum
    
# RomanToInt('DCXXI')
evaluate_test_cases(RomanToInt,tests)
