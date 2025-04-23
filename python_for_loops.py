# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

string = "A foolish consistancy is the hobgoblin of a little mind."

# for letter in string:
#     print(letter)

cars = ["Ford", "Chevy", "Jeep"]
 

#  Break statements terminate a loop BEFORE a matching codition is found. 
for car in cars:
    if car == "Chevy":
        break
    print(car)

instruments = ["piano", "guitar", "saxophone"]

for instrument in instruments: 
    # if instrument == "guitar":
    #     continue
    print("Instrument:           ", instrument)

# To loop through a set of code a specified number of times, we can use the range() function,

# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

for x in range(6):
    print(x)

print("__________________________________________")

for y in range(2, 6):
    print(y)

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter
print("__________________________________________")


# The increment value is the last argumen tto be passed into the range() method. 
for x in range(2, 30, 3):
    print(x)
else: 
    print("Finished!")

print("__________________________________________")

for x in range(6):
    if x == 3:
        break
    print(x)
else: 
    print("Finally finished!")

# Nested Loops
# The "inner loop" will be executed one time for each iteration of the "outer loop

print("__________________________________________")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

print("__________________________________________")

singles = [1,2,3]
tens = [1,2,3]

for x in tens:
    for y in singles:
        print( x, y)

for letter in "string":
    pass