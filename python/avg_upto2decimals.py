if __name__ == '__main__':
    student_marks = {}
    for _ in range(int(input())):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks = student_marks[query_name]
    avg = (sum(marks))/len(marks)
    print(f"{avg:.2f}")
