from math import sqrt
# this imports only the function sqrt
print sqrt(25)

""" another alternative would be 'import math'
and then 'print math.sqrt(25)' """

""" another alternative would be 'universal import'
'from math import *'
Note: this is not recommended because you don't know
which functions you're getting """

everything = dir(math)
print everything
# to see what functions are in an imported module
