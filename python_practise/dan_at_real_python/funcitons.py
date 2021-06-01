# Functions are first-class citizens in Python:

# They can be passed as arguments to other functions,
# returned as values from other functions, and
# assigned to variables and stored in data structures.

def myfunc(a, b):
    return a + b

funcs = [myfunc]
funcs[0]
#<function myfunc at 0x7f8b13c6b670>
funcs[0](2, 3)
#5
