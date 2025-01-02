n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))


def quick_desc(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[0]
    tail = numbers[1:]

    left = [x for x in tail if x > pivot]
    right = [x for x in tail if x <= pivot]

    return quick_desc(left) + [pivot] + quick_desc(right)


print(quick_desc(numbers))
