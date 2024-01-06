if __name__ == '__main__':
    res = []
    marks = []
    for i in range (int(input())):
        name = input()
        score = input()
        res.append([name,float(score)])
        marks.append(float(score))
    marks = sorted(set(marks))
    x = marks[1]
    name = []
    for val in res:
        if x == val[1]:
            name.append(val[0])
    name.sort()
    for nm in name:
        print(nm)
