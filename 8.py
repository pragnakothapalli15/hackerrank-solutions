n = int(input())
students = []
for _ in range(n):
    name = input()
    score = float(input())
    students.append([name, score])

scores = sorted(set([student[1] for student in students]))
second_lowest_score = scores[1]
second_lowest_students = sorted([student[0] for student in students if student[1] == second_lowest_score])
for name in second_lowest_students:
    print(name)