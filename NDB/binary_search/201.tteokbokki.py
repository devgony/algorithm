# n, m = map(int, input().split())
# tteoks = map(int, input().split())
n, m = 4, 6
tteoks = [19, 15, 10, 17]
max = max(tteoks)


def search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    result = cut(array, mid)
    if result == target:
        return mid
    elif result < target:
        return search(array, target, start, mid-1)
    else:
        return search(array, target, mid+1, end)


def cut(tteoks, target):
    return sum(tteok - target if tteok > target else 0 for tteok in tteoks)


result = search(tteoks, m, 0, max)
print(result)
