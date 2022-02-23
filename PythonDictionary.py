# Python Beginners Tutorial | Collections DICTIONARY | Basic Programming 8
# Dictionary {K:V} unordered | changeable | indexed | no duplicates
my_dict = {
    "class": "animal",
    "name": "giraffe",
    "age": 10
}

print(my_dict)  # {'class': 'animal', 'name': 'giraffe', 'age': 10}
print(my_dict["name"])  # giraffe
print(my_dict.get("name"))  # giraffe
print(my_dict.values())  # dict_values(['animal', 'giraffe', 10])

for x in my_dict:
    print(my_dict[x])  # x = key
# animal
# giraffe
# 10

for x, y in my_dict.items():  # x = key and y = value.
    print(x, y)
# class animal
# name giraffe
# age 10

my_dict["name"] = "elephant"
print(my_dict)  # {'class': 'animal', 'name': 'elephant', 'age': 10}

# You can add a new key and value.
my_dict["color"] = "grey"  # {'class': 'animal', 'name': 'elephant', 'age': 10, 'color': 'grey'}
print(my_dict)

my_dict.pop("color")
print(my_dict)  # {'class': 'animal', 'name': 'elephant', 'age': 10}

my_dict.popitem()
print(my_dict)  # {'class': 'animal', 'name': 'elephant'}

del my_dict["class"]
print(my_dict)  # {'name': 'elephant'}

# Remove all items.
my_dict.clear()
print(my_dict) # Output: {}

# Delete the dictionary itself
del my_dict

