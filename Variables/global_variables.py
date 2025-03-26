# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.

x = "awesome"
y = 'awesome'


def my_func_global_variable(): 
    print("python is " + x)
    
# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
    
def my_func_local_variable():
    x = "fantastic"
    print("Python is " + x)
    
my_func_global_variable()
my_func_local_variable()

# The Global Keyword

# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

# To create a global variable inside a function, you can use the global keyword.

def my_func_global_keyword(): 
    global nifty
    nifty = "nifty"
    
my_func_global_keyword()

print("Python is " + nifty)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
a = "dumb"

def new_func(): 
    global a 
    a = "cool"
    
new_func()

print("Python is " + a)


