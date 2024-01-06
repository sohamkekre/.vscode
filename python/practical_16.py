file = open('example.txt','w')
file.write("This is the write command\n")
file.write("It allows us to write in a particular")
file.close()

file = open('example.txt','r')
for each in file:
    print(each)
    
file = open('example.txt','a')
file.write("\nThis will add this line")
file.close()
