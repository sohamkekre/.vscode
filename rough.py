n = int(input())
otp = 0
for i in range(n):
    operations = str(input())
    if '--' in operations :
        otp -= 1
    else :
        otp += 1
print(otp)