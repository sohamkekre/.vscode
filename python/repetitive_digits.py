n1 = int(input("enter the n1: "))
n2 = int(input("enter the n2: "))

def repetitive_digits(n1,n2):
    count = 0
    for number in range(n1,n2+1):
        num_str = str(number)
        seen_digits = ""
        for digit in num_str:
            if digit in seen_digits:
                count += 1
                break
            else:
                seen_digits += digit
    unrepeated_count = (n2+1)-n1-int(count)
    print(unrepeated_count) 

repetitive_digits(n1,n2)