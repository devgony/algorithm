def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


array = [1, 2, 3, 4, 5, 6, 7]
result = binary_search(array, 6, 0, len(array) - 1)
print(result)
