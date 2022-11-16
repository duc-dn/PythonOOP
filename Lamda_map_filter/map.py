def mutiply(x):
    return x * x 


data = [1, 3, 5, 6, 7]
result = map(mutiply, data)
print(list(result))



res = map(lambda x: x * x, data)
print(list(res))