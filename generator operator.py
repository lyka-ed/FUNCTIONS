# ----------------------------------------------------------

# ------------** GENRATOR OPERATOR **------------
  
""" when working  with large data "DO NOT STORE IN MEMORY"
instead store data using a generator obeject. It can be iterated over. """

from sys import getsizeof

# --------------- ** EXAMPLE 1 ->>> Generator object
numbers = (a * 2 for a in range(20))
print(numbers)
print(type(numbers))  # it shows the class type which is a generator

for a in numbers:
    print(a)


# --------------- ** EXAMPLE 2 - >>> List Comprehension
digits = [a * 2 for a in range(20)]
print(digits)           # here digits are in a list format.
print(type(digits))     # class 'list'

for a in digits:
    print(a)            # It's out of the list
 
 
# --------------- ** EXAMPLE 3 - >>> Getting the size of the generator object
#  the getsizeof() was inported in already.
# numbers = (a * 2 for a in range(20))
# numbers = (a * 2 for a in range(200))
# numbers = (a * 2 for a in range(2000))
# numbers = (a * 2 for a in range(20000))
# numbers = (a * 2 for a in range(200000))

"""
from the above it's notices that storing large data or working with infinte stream
such as Facebook, Twitter, etc 
"""

print("Generator_Operator", getsizeof(numbers))

# --------------- ** EXAMPLE 4 - >>> Getting the size of the list comprehension  
#  same goes for here too
digits = [a * 2 for a in range(20)]
# digits = [a * 2 for a in range(200)]
# digits = [a * 2 for a in range(2000)]
# digits = [a * 2 for a in range(20000)]
# digits = [a * 2 for a in range(200000)]
# digits = [a * 2 for a in range(2000000)]

""" size of a List comprehension  keeps increasing consistently based of the datas being stored in it
"""
print("List_Comprehension", getsizeof(digits))
