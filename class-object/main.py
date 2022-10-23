class Dog:
    # class attribute: các thuộc tính chung của 1 lớp (có thể hiểu là những cái chung)
    # hay còn gọi là class varriable (một biến dùng chung cho tất cả các đối tượng thuộc class đó)
    # nó không gắn với bất kỳ đối tượng nào mà chi gắn với lớp đó
    attr1 = "mamal"

    # instance class methods
    def __init__(self, name):
        # instance attribure: các thuộc tính của 1 cá thể của lớp đó
        self.name = name

    def bark(self, bark: str):
        print(self)
        print("Bark: " + bark)

# ============= self =============
# Khi chúng ta gọi một method của đối tượng đó vd Rodger.bark(arg1)
# Nó sẽ tự động chuyển thành Rodger.bark(Rodger, arg1)

# object instantiation
Rodger = Dog("Rodger")

# accessing class attributes
print(Rodger.__class__.attr1)

# accessing instance attributes
print("My name is {}".format(Rodger.name))

# accessing class methods
Rodger.bark("gâu gâu")

