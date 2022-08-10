# n, m, k = map(int, input().split())
n, m, k = [5, 8, 3]
# numbers = list(map(int, input().split()))
numbers = [2, 4, 5, 4, 6]
first, second, *rest = sorted(numbers, reverse=True)
result = 0
while m > 0:
    if m > k:
        result += first * k + second
        m -= k + 1
    else:
        result += first * m
        m = 0

print(result)

# Answer
# # n, m, k = map(int, input().split())
# n, m, k = [5, 8, 3]
# # numbers = list(map(int, input().split()))
# numbers = [2, 4, 5, 4, 6]
# first, second, *rest = sorted(numbers, reverse=True)
# num_first = (m // (k+1)) * k + m % (k+1)
# result = 0
# result += num_first * first
# result += (m - num_first) * second

# print(result)
