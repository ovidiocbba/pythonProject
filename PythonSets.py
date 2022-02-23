# Python Beginners Tutorial | Collections SETS | Basic Programming 7
# Set {} unordered | unindexed | no duplicates
my_set = {"Chalk", "Duster", "Board"}
print(my_set)

for x in my_set:
    print(x)

print("Chalk" in my_set)

my_set.add("Pen")  # {'Pen', 'Board', 'Duster', 'Chalk'}
print(my_set)
my_set.update(["Pencil", "Eraser"])  # {'Pencil', 'Chalk', 'Pen', 'Board', 'Duster', 'Eraser'}
print(my_set)

len(my_set)
my_set.remove("Pencil")  # {'Duster', 'Board', 'Eraser', 'Pen', 'Chalk'}
print(my_set)

my_set.discard("Pen")  # {'Chalk', 'Duster', 'Eraser', 'Board'}
print(my_set)

# my_set.remove("Pencil")  # KeyError: 'Pencil'
my_set.discard("Pen")

my_set.pop()  # Remove and return an arbitrary set element.
print(my_set)

my_set.clear()
print(my_set)  # set()

del my_set

my_set_2 = {"Apples", 1, 2, (3, 4, 5)}
print(my_set_2)  # {1, 2, (3, 4, 5), 'Apples'}

my_list = [1, 2, 3]
print(my_list)  # [1, 2, 3]

my_set_3 = set(my_list)
print(my_set_3)  # {1, 2, 3}

# Mathematical expressions.
# UNION | INTERSECTION | DIFF | SYMMETRIC DIFF
A = {'A', 'B', 1, 2, 3}
B = {'B', 'C', 3, 4, 5}
# Combine all elements from A and B.
print(A.union(B))  # {1, 2, 3, 4, 5, 'B', 'C', 'A'}
# The symbol for union is '|'
print(A | B)

# The common elements from A and B.
print(A.intersection(B))  # {3, 'B'}
print(A & B)

print(A.difference(B))  # {1, 2, 'A'}
print(A - B)

print(A.symmetric_difference(B))  # {1, 2, 4, 5, 'A', 'C'}
print(A ^ B)
