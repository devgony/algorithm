# n, k = map(int, input().split())
# data1 = list(map(int, input().split()))
# data2 = list(map(int, input().split()))

n, k = 5, 3
data1 = [1, 2, 5, 4, 3]
data2 = [5, 5, 6, 6, 5]

data1.sort()
data2.sort(reverse=True)

min3 = data1[:3]
max3 = data2[:3]

max_data = []
for a, b in zip(min3, max3):
    if b > a:
        max_data.append(b)
    else:
        max_data.append(a)

max_data += data1[3:]

print(sum(max_data))
