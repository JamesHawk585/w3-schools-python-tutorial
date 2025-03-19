
import random


string = 'a foolish constistancy is the hobgoblin of a little mind'

print(string[2:5])
print(len(string))



def print_string():
    random_element = random.randrange(1, 56)
    print('inside print_string()')
    print(string[random_element])

print_string()



print(string[:18])
print(string[18:])
