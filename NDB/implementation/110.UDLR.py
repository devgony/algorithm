n = int(input())
plans = input().split()
space = [[0] * n for _ in range(n)]

x = 1
y = 1

for plan in plans:
    if plan == 'U' and x > 1:
        x -= 1
    elif plan == 'D' and x < n:
        x += 1
    elif plan == 'L' and y > 1:
        y -= 1
    elif plan == 'R' and y < n:
        y += 1

print(x, y)
