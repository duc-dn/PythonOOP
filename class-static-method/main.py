# class method

# Python program to demonstrate
# use of class method and static method.
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        print(cls)
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18

person1 = Person("Duc", 22)
person2 = Person.fromBirthYear("Duc", 2001)

print(person1.age)
print(person2.age)

print(person1.isAdult(person1.age))