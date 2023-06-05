days = {"Month", "Year"}

def print_member(iterable):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break
        else:
            print(item)

print_member({1,2,3, 4})