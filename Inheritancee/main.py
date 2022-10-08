# Parent class
class Person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))

# Child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        Person.__init__(self, name, idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("Idnumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))

a = Employee('Rahul', 886012, 200000, "Intern")

# # call class methods
a.display()
print("-----------------------", end="\n")
a.details()

print(isinstance(a, Employee))
print(issubclass(Employee, Person))
