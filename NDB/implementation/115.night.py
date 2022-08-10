y, x = list(input())
ys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
y = ys.index(y)
x = int(x) - 1
result = 0

cases = [
    (x - 2, y - 1),
    (x - 2, y + 1),
    (x + 2, y - 1),
    (x + 2, y + 1),
    (x - 1, y - 2),
    (x - 1, y + 2),
    (x + 1, y - 2),
    (x + 1, y + 2),
]

for (x, y) in cases:
    if 0 <= x <= 7 and 0 <= y <= 7:
        result += 1

print(result)
