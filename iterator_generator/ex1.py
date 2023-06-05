def square_generator(n):
    for i in range(1, n+1):
        yield i**2

def square_sum_return(n):
    squares = [i**2 for i in range(1, n+1)]
    return sum(squares)

generator = square_generator(1000000)
print(type(generator))
print("sum: {}".format(sum(generator)))