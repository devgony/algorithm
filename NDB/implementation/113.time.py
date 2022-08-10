n = int(input())
secs = list(range(0, 60))
mins = list(range(0, 60))
hours = list(range(0, n+1))

result = 0
for hour in hours:
    for min in mins:
        for sec in secs:
            time = f"{hour}:{min}:{sec}"
            if "3" in time:
                result += 1

print(result)
