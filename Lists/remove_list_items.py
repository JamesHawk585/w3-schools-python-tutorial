# The remove() method removes the specified item.

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove the first occurrence of "banana":
fruitlist = ["apple", "banana", "cherry", "banana", "kiwi"]
fruitlist.remove("banana")
print(fruitlist)

poplist = [1,2,3,4,5,6,7,8,9]
poplist.pop(-1)
print(poplist)

letterlist = ["a", "b", "c", "d"]

# If no index is specified, pop() will return the last index in a list. 
print(letterlist.pop())
backward_letter_list = ["z", "y", "x"]

del backward_letter_list[0]
