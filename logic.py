def rank_students(data):
    # Sort based on total marks using Bubble Sort
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            total1 = sum(data[j][2:])
            total2 = sum(data[j+1][2:])
            if total1 < total2:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def average_marks(data):
    total = [0, 0, 0]
    for student in data:
        total[0] += student[2]
        total[1] += student[3]
        total[2] += student[4]
    count = len(data)
    return [round(t / count, 2) for t in total]
