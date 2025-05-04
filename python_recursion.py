# Python accept function recursion. 

# Recursion is a common mathmatical and programming concept. It means that a function can call itself. This has the benefit of allowing you to loop through data to reach a result.  

# Incorrectlyimplemented recursion can easily result in an infite loop. 

# In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

# To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.

import ipdb 

def tri_recursion(k):
    if (k > 1):
        result = k + tri_recursion(k - 1)
        print(result)
        # ipdb.set_trace()
    else: 
        result = 0
        # ipdb.set_trace()
    return result

print("Recursion Example Results: ")
tri_recursion(3)

