# 14. Create a python file and import some of the functions from the above 13 tasks and try to use them.
from functions1 import *

print(has_33([1, 3, 3])) #    True
print(has_33([1, 3, 1, 3])) # False
print(has_33([3, 1, 3])) #    False

print(spy_game([1,2,4,0,0,7,5])) # True
print(spy_game([1,0,2,4,0,5,7])) # True
print(spy_game([1,7,2,0,4,5,0])) # False

histogram([4, 9, 7])
# ****
# *********
# *******

reverse_string("We are ready") # ready are We