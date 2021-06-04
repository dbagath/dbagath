from functools import reduce 

lst = [2, 3, 4, 5]

lst = list(map(lambda x: x ** 2, lst))

print(lst)

lst = [10, 5, 5, 5]

lst = reduce(lambda x, y: x + y, lst)

print(lst)

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

over_75 = list(filter(lambda x: 80 > x > 60, scores))

print(over_75)