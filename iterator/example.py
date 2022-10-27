class PowTwo:
    def __init__(self, m = 0) -> None:
        self.max = m
    
    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n 
            self.n += 1
            return result
        else:
            raise StopIteration

a = PowTwo(4)
i = iter(a)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
