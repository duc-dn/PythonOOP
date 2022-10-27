def gen():
    yield 'Kteam'
    print('This is the second yield')
    yield 'Fress education'
    print('This is the last yield')
    yield 'Duc dep trai'
    print("Will not return anything")

for value in gen():
    print(value)