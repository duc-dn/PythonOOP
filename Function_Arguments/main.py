def variableLengthArgExample(a, b, *args):
    print(a, b)
    print(*args)
    print(f'Type of *args: {str(type(*args))}')


if __name__ == "__main__":
    variableLengthArgExample(1,2, (1,2,3,4))