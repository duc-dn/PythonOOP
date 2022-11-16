data = [1, 2, 5, 6, 7, 8, 3]

res = filter(lambda x: x % 2 == 0, data)
print(list(res))