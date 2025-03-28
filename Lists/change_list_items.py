thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
newlist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
newlist[1:3] = ["blackcurrant", "watermelon"]
print(newlist)

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

mylist = ["apple", "banana", "cherry"]
mylist[1:2] = ["tomato", "corn"]
print(mylist)

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

listylist = ["apple", "banana", "cherry"]
listylist[1:3] = ["Watermelon"]
print(listylist)

numlist = [1,2,3,4,5,6,7,8,9]

numlist[4:6] = ["testing", "testing", "testing"]
print(numlist)
print(len(numlist))
print(bool(len(numlist) == 10))

insertedlist = ["Toyota", "Chevrolet", "Ford"]
insertedlist.insert(2, 100)
insertedlist[1] = "I am an inserted string"
print(insertedlist)