# "is" vs "=="

a = [1, 2, 3]
b = a

a is b
#True
a == b
#True

c = list(a)

a == c
#True
a is c
#False

# • "is" expressions evaluate to True if two 
#   variables point to the same object

# • "==" evaluates to True if the objects 
#   referred to by the variables are equal
