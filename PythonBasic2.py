# Python Beginners Tutorial | If Else Loops| Basic Programming 2
if 5 > 3:
    print("5 is greater than 3")
num = 1
if num > 0:
    print("This is a positive num")
else:
    print("This is a negative num")

# Elif
num = 0
if num > 0:
    print("This is a positive num")
elif num == 0:
    print("Num is zero")
else:
    print("This is a negative num")

# For
num = [1, 2, 3, 4, 5]
for val in num:
    print(val)

# For
num = [1, 2, 3, 4, 5]
sum = 0
for val in num:
    sum = sum + val
print("Total is", sum)  # Total is 15

# For
fruits = ["apple", "oranges", "grapes"]

for val in fruits:
    print(val)
else:
    print("No fruits left")

# While
print("Enter a number: ")
num = int(input())
sum = 0
i = 1

while i < num:
    sum = sum + i
    print(sum)
    i = i + 1
print("Total is :", sum)
