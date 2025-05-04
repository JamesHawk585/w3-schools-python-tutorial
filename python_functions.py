import random

# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.



def my_function(first_name, last_name):
    # print(first_name + " " + last_name)
    print(f'{first_name} {last_name}')

my_function("James", "Hawk")
my_function("Hawk", "James")
my_function("John", "Doe")
my_function("Gerorge", "Washington")

terminal_line_break = "__________________________________"

print(terminal_line_break)

def sentence_function(*kids):
    print("The youngest child is " + kids[3])


# pass any number of arguments into sentence_function. The function will index the argument values like a list. 

sentence_function("James", "John", "Julie", "Jarred", "Jason")

print(terminal_line_break)

# You can also send values with *key = value* syntax. 

def new_func(child3, child2, child1):
    print("The youngest child is " + child3)

# YOu can pass in as many values as you want. 
# Passing it too few values results in a TypeError. 

# new_func(child3="Timmy")

# PAss in all arguments into the function call that are passed into the function definition,even if the values go unused. 

new_func(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# You can specificy that your function will have ONLY positional or ONLY keyword arguments. 

# To specifity that a function can have only positonal arguments, add / after the args.Adding too mny args will throw a TypeError. 


def my_keyword_function(x, /):
    print(x)


my_keyword_function(3)

# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:

# my_keyword_function(x = 5)

# To specify that a function can have only keyword arguments, add *, before the arguments:

def my_positional_function(*, x):
    print(x)

my_positional_function(x = 3)