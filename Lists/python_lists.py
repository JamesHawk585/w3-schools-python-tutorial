thislist = ["apple", "banana", "cherry"]

print(thislist[0])
print(thislist[-1])

# Lists allow duplicate values:
# Python variables can be redeclared

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# String, int and boolean data types:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# A list with strings, integers and boolean values:
list1 = ["abc", 34, True, 40, "male"]

# From Python's perspective, lists are defined as objects with the data type 'list':
print(type(list1))

# It is also possible to use the list() constructor when creating a new list.
constructed_list = list(("apple", "banana", "cherry")) # Note the double parenthesis

# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.