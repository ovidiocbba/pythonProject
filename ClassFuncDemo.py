# Python Beginners Tutorial | Classes Functions Objects | Basic Programming 4
class MyClass:
    name = 'Raghav'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sum(self, a, b):
        print(a + b)


x = MyClass("John", 40)
print(x.name)
print(x.age)
x.sum(4, 5)
del x
