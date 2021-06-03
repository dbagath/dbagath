from functools import reduce 

lst = [2, 3, 4, 5]

lst = list(map(lambda x: x ** 2, lst))

print(lst)

lst = [10, 5, 5, 5]

lst = reduce(lambda x, y: x + y, lst)

print(lst)