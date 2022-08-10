# # n,m=map(int,input().split())
# n, m = 4, 4
# x, y, d = 1, 1, 0
# directions = [
#     (0, -1),
#     (1, 0),
#     (0, 1),
#     (-1, 0)
# ]
# minimap = [
#     [1, 1, 1, 1],
#     [1, 0, 0, 1],
#     [1, 1, 0, 1],
#     [1, 1, 1, 1]
# ]


# def turn(cur):
#     # 0 => 3 => 2 => 1
#     if cur > 0:
#         return cur - 1
#     else:
#         return 3


# cache = [x, y]
# while True:
#     cur = (x, y)
#     for _ in range(4):
#         d = turn(d)
#         dx, dy = directions[d]
#         nx, ny = x + dx, y + dy
#         if minimap[nx][ny] == 0 and not (nx, ny) in cache:
#             cache.append((nx, ny))
#             x, y = nx, ny
#             break
#     if cur == (x, y):
#         break

# result = len(cache)
# print(result)


# # Answer
# n, m = map(int, input().split())
# d = [[0] * m for _ in range(n)]
# x, y, direction = map(int, input().split())
# d[x][y] = 1
# _map = []
# for i in range(n):
#     _map.append(list(map(int, input().split())))
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]


# def turn():
#     global direction
#     direction -= 1
#     if direction == -1:
#         direction = 3


# count = 1
# num_turned = 0
# while True:
#     turn()
#     nx = x + dx[direction]
#     ny = y + dy[direction]
#     if d[nx][ny] == 0 and _map[nx][ny] == 0:
#         d[nx][ny] = 1
#         x, y = nx, ny
#         count += 1
#         num_turned = 0
#         continue
#     else:
#         num_turned += 1
#     if num_turned == 4:
#         nx = x - dx[direction]
#         ny = y - dy[direction]
#         if _map[nx][ny] == 0:
#             x, y = nx, ny
#         else:
#             break
#         num_turned = 0

# print(count)
