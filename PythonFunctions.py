# Python Beginners Tutorial | Python Functions | Basic Programming 3.
# Functions.
def printHello():
    print("Hello")


printHello()


# With a parameter.
# def printHi(name):
# With Default parameter0
def printHi(name="John"):
    print("Hi, " + name)


printHi("Raghav")
printHi()


# Functions
def sum(a, b, c):
    print(a + b + c)


sum(10, 20, 30)


def returnSum(a, b):
    """ This is a function to calculate sum of 2 numbers"""
    return (a + b)


x = returnSum(10, 20)
print(x)
