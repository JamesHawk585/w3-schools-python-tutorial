# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType


import random

x = 5
y = 20
a = float(x)
b = int(y)

# print(type(x))
# print(type(y))
# print(a, b)

print(random.randrange(1, 100))

print(random.randrange(500, 1000))

hello_world = "Hello World!"

# print(hello_world[6])

# Since strings are arrays, we can loop through the characters in a string, with a for loop.

for element in "banana":
    print(element)

# print(len('banana'))


string = "The old wooden pier stretched out into the misty lake, its weathered planks creaking softly in the morning breeze. A lone fisherman sat at the far end, his silhouette barely visible through the veil of fog that rose from the waters surface. The sun was slowly climbing above the treetops, painting the sky in hues of deep purple and orange, its rays catching the mist and turning it into a thousand dancing diamonds. A small wooden boat bobbed gently against the piers pilings, its rope creating a rhythmic slapping sound against the hull. As the light grew stronger, it illuminated the surrounding forest, where birds were beginning to stir in their nests, their morning songs filling the crisp air. The fisherman cast his line into the water, the ripples from the splash disturbing the perfect mirror image of the trees and sky, creating ever-widening circles that slowly disappeared into the depths of the lake."

# 'in' keyword
print('grew' in string)
print('aluminum' in string)

# if statement
if 'grew' in string:
    print('grew in string')
    
    print(type(hello_world))
