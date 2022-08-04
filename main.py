list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 8, 10]
result = map(lambda a, b: a+b, list1, list2)
print(list(result))
