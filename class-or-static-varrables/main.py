class CSStudent:
    stream = 'cse'           # class variable or static variable
    def __init__(self, name, roll):
        self.name = name     # instance variable
        self.roll = roll     # instance variable

# objects of CSSstudent class
a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)

print('--------------------')
print(a.stream)
print(b.stream)

# class variables can be accesed using class
print(CSStudent.stream)

print('--------------------')
print("Now if we change the stream for just a it won't be changed for b")
a.stream = 'ece'
print(a.stream) # prints 'ece'
print(b.stream) # prints 'cse'

print('--------------------')
# To change the stream for all instances of the class we can change it
# directly from the class
CSStudent.stream = 'mech'

print(a.stream)  # prints 'ece'
print(b.stream)  # prints 'mech'
c = CSStudent('duc', 3)
print(c.stream)