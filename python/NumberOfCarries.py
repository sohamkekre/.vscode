def NumberOfCarries(num1,num2):
    pass
    carry = 0
    carry_count = 0
    while num1 > 0 and num2 > 0:
        a = num1%10
        b = num2%10
        
        total  = a + b + carry

        if total > 9:
            carry = 1
            carry_count += 1
        else: 
            carry = 0            
        num1 //= 10
        num2 //= 10
    print(carry_count)

NumberOfCarries(451,349)