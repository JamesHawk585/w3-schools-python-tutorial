thislist = ["guitar", "bass", "keyboard"]
thislist.append("Kazoo")
print(thislist)

fruitlist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(fruitlist)

tropical = ["mango", "pineapple", "papaya"]

fruitlist.extend(tropical)
print(fruitlist)

# Add elements of a tuple to a list:
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
a = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")

a.extend(thistuple)
print(a)