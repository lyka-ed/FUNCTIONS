#  --------------------------------------

# ----------** UNPACKING OPERATORS ** ---------
"""
this has to do with unpacking oerator without using their syntax 
The " * " sign is used while unpacking a dict the " ** " is used in front of the variable name.
single star sign
double star sign
"""

# --------------- ** EXAMPLE 1 ->>>> Unpacking List
values = [2, 7, 99, 100, 3, 35]
print(*values)

digits = (range(15))
print(digits)       # gives (0, 15), convert it to a list

digits = list(range(15))
print(digits)
print(*digits)           #List gets unpacked


# --------------- ** EXAMPLE 2 ->>>> Unpacking Dictionary with different key value
user_info_1 = {
    "Surname": "Patrick",
    "City": "Lagos"
}

user_info_2 = {
    "Name_2": "Benard",
    "Age_2": 40
}

user_info_3= {
    "Name": "Alex",
    "Sex": "Male"
}


combined_info = {**user_info_1, **user_info_2, **user_info_3}
print(combined_info)

# --------------- ** EXAMPLE 3 ->>>> Unpacking Dictionary with similar key value
"""
In this case upacking a dict that has the same value name, python will only print 
one set of the user_profile with its key value and items 
"""
user_profile_1 ={
    "Name": "Lyka Edem",
    "Age": 22,
    "Sex": "Female"
}

user_profile_2 = {
    "Name": "Jennifer Ezike",
    "Age": 27,
    "Sex": "Female"
}

user_profile_3 = {
    "Name": "Captain Alex",
    "Age": 29,
    "Sex": "Male"
}

combined_profile ={**user_profile_1, **user_profile_2, **user_profile_3}
print(combined_profile)


# --------------- ** EXAMPLE 3 ->>>> Combining a List
names = ["Daniel", "Precious", "Emmanuella", "Fedora"]
ages = [19, 16, 10, 7]
combined_list = [*names, *ages]
print(combined_list)



















