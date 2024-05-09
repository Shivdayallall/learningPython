import random

"""
-Python version of an array is  List.
-created using []
"""
fruits = ["apple", "grapes", "banana", "peach", "blue-berry", "pine-apple"]
fruits.append("plum")  #add item to end of list

# pick a random name out of a list
names = ["billy", "bob", "timmy"]

num_items = len(names)
random_choice = random.randint(0, num_items - 1)
print(f"{names[random_choice]} is buying lunch")


