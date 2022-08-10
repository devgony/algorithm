# n, m = map(int, input().split())
# data = []
# for _ in range(n):
#     data.append(list(map(int, input().split())))
n, m = 3, 3
data = [
    [3, 1, 2], [4, 1, 4], [2, 2, 2]
]

mins = []
for i, row in enumerate(data):
    mins.append((i, min(row)))
result = max(mins, key=lambda x: x[1])[0]
print(result)
