print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if a > b: 
    print("a is greater than b")
else: 
    print("a is not bigger than b")
    
print(bool("hello"))
print(bool(15))
print(bool(""))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:

class my_class():
    def __len__(self):
        return 1
    
my_obj = my_class()
print(bool(my_obj))

def my_function():
    return True

print(my_function())

if my_function():
    print("YES!")
else: 
    print("NO!")
    


x = 200
print(isinstance(x, int))
