# ----------------------------------------------------------
# ---------------** ## MAP FUNCTIONS ## **------------------

""" 
Map() performs similar case as the filter()
it accepts both >>> iterables and function, meaning 2 arguments must be passed
A map function object must always be converted to atleast one data types

"""
# ----------->>>> EXAMPLE 1 
# set_of_num = (1, 2, 3, 4, 5)   #iterables
# def calculate_square(x):       #fuctions
# #     return x * x    
    
# result = map(calculate_square, set_of_num) 
# print(result)   

# # A map object can be >>> to at least one data type >> a set, tuples and list
# # Set
# num_square = set(result)
# print(num_square)

# # list
# num_square = list(result)
# print(num_square)      
#in this case this result appears as an empty list >> [ ] cause the data was already print in a set format

# ----------->>>> EXAMPLE 2: Lambda + Map()
num_1 = (1, 2, 3, 4, 5)
vowels = ['a', 'e', 'i']

result = map(lambda x: x, vowels)
print(result)

# letters converted to a set
vowelSets = set(vowels)
print(vowelSets)


# ----------->>>> EXAMPLE 2: Passing more than 1 iterable in a Map()
number1 = [1, 2, 3, 4, 5]
number2 = [7, 8]
result = map(lambda n1,n2 : n1 + n2, number1, number2)
print(type(result))


