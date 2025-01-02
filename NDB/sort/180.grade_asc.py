n = int(input())
grades = []
for i in range(n):
    name, grade = input().split()
    grades.append((name, int(grade)))

counts = [0] * (max(grades) + 1)

for name, grade in grades:
    counts[grade] += 1
