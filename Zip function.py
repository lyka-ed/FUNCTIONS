# -------------- ZIP FUNCTION -------------
"""
In a zip() iterables are passed, zero and more.
Aggregates in a tuples and returns.
"""
# --------------- ** EXAMPLE 1 ** ---------
from traceback import print_tb
from unittest import registerResult


names_list = ['Alex', 'Benita', 'Danny']
number_list = [1, 2, 3]

# looking into various cases where zip() can be used.
# CASE 1 -->>> when no iterable is passed

result = zip()
# at this point converting the iterator into a list

new_result = list(result)
print(new_result)      # result to []

# CASE 2 -->>> when two iterables are passed
result = zip(names_list, number_list)
print(result)
#  converting to a set
result_set = set(result)
print(result_set)

# CASE 3 -->>> when different numbers of iterables are passed
list_Of_numbers = [1, 54, 23, 0, 9, 6, 2, 12, 34, 100]
list_Of_names = ["Alex", "Jenny", "Bliss"]
numbers_In_tuples = ("ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX")

result = zip(list_Of_numbers, list_Of_names, numbers_In_tuples)
print(result)
# converting to a list

result_list = list(result)
print(result_list)
""" 
From the print(result_list), you will noticed that not all the values was printed
reason being that in a zip() the rules states that iteration continues untill the
shortest arguement is exhausted ..from the  list_Of_nmaes had the least items 
"""

# --->>> UNZIPPING VALUES USING zip()
coordinates = ['x', 'y', 'z']
values = [ 8, 2, 0 ]
result = zip(coordinates, values)
print(result)

# as usual convert from zip object 
result_list = list(result)
print(result_list)

