def Beautiful_matrix():
    matrix = []
    for i in range(5):
        line = list(map(int,input().split(" ")))
        matrix.append(line)
    # print(matrix)
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 1:
                one_cordinates = [i,j]
                # print(f"one_cordinates: {one_cordinates}")
                break
            else:
                continue
    primary_cordinates = [2,2]
    x = one_cordinates[0] - primary_cordinates[0]
    y = one_cordinates[1] - primary_cordinates[1]
    if x < 0:
        x = -(x)
    if y < 0:
        y = -(y)
    center = x + y
    return center

print(Beautiful_matrix())

# 1 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0