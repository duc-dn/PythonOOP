# Special function là một hàm đặc biệt trong python, bắt đầu với đấu gạch dưới __
# Các hàm đặc biệt goups chúng ta định nghĩa một số method, perator được định nghĩa sắn trong python
# VD: __str__, ...
# Cũng có thế hiểu là nạp trồng
# Có nhiều hàm special function

class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "Test a: %s, b: %s" % (self.a, self.b)

    def __str__(self):
        return "From str method of Test: a is %s," \
               "b is %s" % (self.a, self.b)

t = Test(4, 5)
print(t) # This calls __str__()
print([t]) # This calls __repr__()