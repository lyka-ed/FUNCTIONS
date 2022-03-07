# ----------------------------------------------------------
# ----------------** ## THE FILTERED FUNCTION ## **-----------------
""" 
Fuction is a block of code written once and excuted everywhwere
it can hold a unit
"""
""" 
The filterd functions accepts two(2) parameters (Functions, Iterables).
Filtered fuctions also give attributes with the help of a fuction that tests each element in the iterable to be True or False
"""

# --------------- ** EXAMPLE 1 ** ---------
# Iterables
alphabets = ['j', 'e', 'i', 'h', 'o', 'w', 'u', 't', 'a']

# Functions
def filtered_vowels(alphabets):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if (alphabets in vowels):
        return True
    else:
        return False  

filtered_vowels = filter(filtered_vowels, alphabets)  
print(filtered_vowels)
print(type(filtered_vowels))


# --------------- ** EXAMPLE 2 ** ---------
unusual_list = [True, '10', False, 1, 0, ]
Filtered_list = filter(None , unusual_list)
print("Truthy values are: ")


# --------------- ** EXAMPLE 3 ** ---------
def my_new_fuction():
    print("Hi, this is my new fuction")

my_new_fuction()    
""" variable defined inside a fuction is called "A LOCAL VARIABLE"
variable defined outside a fuction is called "A GLOBAL VARIABLE" """

user_input = input("Please enter your name: ")

def shout_name(usersName):
    print(f"Haaay {usersName}, come back!!")


shout_name(user_input)

a = input("First num: ")
b = input("Second num: ")

a = int(a)
b = int(b)

def shoutName(x, y):
    answer = x + y
    return answer

dd = shoutName(a,b)
print(dd)





