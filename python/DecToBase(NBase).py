# dic = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',16:'G',17:'H',18:'I',19:'J',20:'K',21:'L',22:'M',23:'N',24:'O',25:'P',26:'Q',27:'R',28:'S',29:'T',30:'U',31:'V',32:'W',33:'X',34:'Y',35:'Z'}

# def DectoNBase(n,num):
#     quotient = 5
#     remainder = 5
#     NBase = ""
#     while quotient >= 1 :
#         quotient = int(num / n)
#         remainder = int(num % n)
#         num = quotient
#         if remainder in dic :
#             if dic.get(remainder) in NBase:
#                 break
#             ch = dic.get(remainder)
#             NBase = ch + NBase
#     print(NBase)            

def DectoNBase(n,num):
    if n < 1 or n > 36:
        return ("Invalid Base")
    if num == 0:
        return ("0")
    
    result = ""
    
    while num>0:
        symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        remainder = num % n

        result  = symbols[remainder] + result
        num //= n

    print(result)


DectoNBase(12,718)