# https://www.youtube.com/watch?v=mqpgfShT61g
# How Does Python Chain Iterables?
# Bring in the chain function
#  from the itertools module.
from itertools import chain
# Create a list of integers, 
#  a string, 
#  and a tuple of integers.
my_list = [1,2,3]
my_str = "fish"
my_tuple = (1.1, 2.2, 3.3, 4.4)
# Itertable through all
#  three iterables 
#  in a single loop 
#  using itertools.chain().
for element in chain(my_list, my_str, my_tuple):
    print(element, 
          end = ", " )
# chain fails if 
#  any of the arguments 
#  are not iterable.
# 42 is not iterable, 
#  so we wrap the call in a 
#  try/except block.
try:
    for element in chain(my_list, 42, my_tuple):
        print(element, 
              end = ", " )
except:
    print("\n An argument is not iterable.")
# This is slick:
# We can create an iterable
#  from our set of iterables.
my_iter = chain(my_list, 
                my_str)
print(f"my_iter is now a {type(my_iter)}")
my_list = list(my_iter)
print(f"my_list is now a {type(my_list)}")
print(f"my_list: {my_list}")
