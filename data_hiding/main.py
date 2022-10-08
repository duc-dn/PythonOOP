# Trong python, we use double underscore trước tên của thuộc tính
# Và các thuộc tính này sẽ không thể nhìn thấy trực tiếp từ bên ngoài (truy cập)

class MyClass:
    # class attribures
    __hiddenVariable = 0

    def add(self, increment):
        self.__hiddenVariable += increment
        print(self.__hiddenVariable)


obj = MyClass()
obj.add(2)
obj.add(5)

# This line error because __hiddentVariable is private varriables
print(obj.__hiddenVariable)

# Tuy nhien, chung ta van co the truy cap den bien do bang tricky syntax
#print(obj._MyClass__hiddenVariable)