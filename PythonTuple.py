# Python Beginners Tutorial | Collections TUPLE | Basic Programming 6
# Tuple () ordered | indexed | unchangeable | duplicates
my_tuple = ("Apples", "Oranges", "Grapes")
print(my_tuple)
print(my_tuple[1])
print(my_tuple[-1])
print(my_tuple[0:3])

for val in my_tuple:
    print(val)

# my_tuple[1] = "Cherry"      # 'Tuple' object does not support item assignment.
# del my_tuple[2]             # 'Tuple' object doesn't support item deletion.

print(len(my_tuple))
my_tuple_2 = ("Banana", (1, 2, 3), ["Tokyo", "New Delhi"])
print(my_tuple_2)
print(my_tuple_2[2][1])

# The list is very mutable. ["Tokyo", "New Delhi"]
my_tuple_2[2][1] = "New York"
print(my_tuple_2)

print("Banana" in my_tuple_2)  # True
print("Cherry" in my_tuple_2)  # False
