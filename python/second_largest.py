n = int(input("Please enter the number "))
s = str(input())
lst = s.split(',')
lst1=[]
print(lst)
for i in lst:
    x = int(i)
    lst1.append(x)
print(lst1)

lst1.pop(lst1.index(max(lst1)))
print(max(lst1))

# ///////OR////// #

input_string = input("Enter the array: ")

number_list = list(map(int,input_string.split(',')))

print(number_list)
