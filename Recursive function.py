# -------------------------------------------------
# ---------- ## RECURSIVE FUNCTION ## -------------

"""
This is a type of function thats calls itself inorder to prevent recursion 
complex task can be broken down ntpo simipler sub portion using recursion
also used in squence generation. Consume memory space and time
"""
import sys 

# --->>>>>>  EXAMPLE 1 

def factorial(x):

    if x == 1:             # back condition
        return 1
    else:
        return(x * factorial(x-1))   # ending condtion

num = 3
num = 5
num = 7
"""
the calculative process in getting the factorial of any number is
3 --->>>> 1 * 2 * 3
5 --->>>> 1 * 2 * 3 * 4 * 5
7 --->>>> 1 * 2 * 3 * 4 * 5 * 6 * 7
"""
print("The factorial number of" ,num, "is", factorial (num) )

print(sys.getrecursionlimit())





