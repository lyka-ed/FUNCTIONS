# ----------------------------------------------------------
# ---------------** ## LAMBDA FUNCTIONS ## **---------------

""" 
Lambda function is also know as "Anonymous"
it is designed without a name
"""
# ----------->>>> EXAMPLE 1 
products = [
    ("Product-1", 15),
    ("Product-2", 45),
    ("Product-3", 25),
    ("Product-4", 5),
    ("Product-5", 20),
    ("Product-6", 30),
]

products.sort(key=lambda product: product[1])
print(products)      # it rearranges in ascending order.

# ----------->>>> EXAMPLE 2 : Lambda + Filter()
my_list = [1, 5, 4, 6, 11, 34, 55, 88]
new_list = filter(lambda x : (x % 2 == 0), my_list)
for num in new_list:
    print(new_list)
    even_num = list(new_list)
    odd_num = list(new_list)
    print(even_num)
    print(odd_num)


