x = (1,2,3)
print(x)
print(*x)

y = {'a': 7, 'b': 8, 'c': 9}
print(*y)

def foo(a, b, c):
    print(a, b, c)

foo(**y)