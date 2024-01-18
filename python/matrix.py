n = int(input("Enter the dimensions: "))
matrix = []
for _ in range(n):
    row = list(map(int,input().split()))
    matrix.append(row)

print(matrix)

for i in range (len(matrix)):
    for j in range (len(matrix[i])):
        if i<j:
            matrix[i][j] = 0

print(matrix)