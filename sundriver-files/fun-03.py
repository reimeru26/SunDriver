b = 'hello'
# This is a program to demonstrate the different namespace inside functions.
def myprint(x):
    # this function prints a string 3 times
    b = 'circular'
    print(x)
    print(x)
    print(x)
    
    print('inside: ', b)
    
    return None # There is no return value here, you could also skip this line.
    
    # block indent defines the end of the function

# here, the function is called (executed)
myprint(b)
print('outside: ', b)


