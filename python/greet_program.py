import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
if int(time.strftime('%H')) < 12 :
    print("Good morning")
elif int(time.strftime('%H')) < 18 :
    print("Good afternoon")
elif int(time.strf('%H')) <= 24:
    print("Good Night")

