# Assignment No 4
# part : 1
# topic :
# 1- Module in python
# 2- Function in python


# 1- Module in python


# what is Module in Python?
# A module is a file containing Python code. It can define functions, classes, and variables that can be reused in other Python programs. Modules help to organize code and promote code reusability.

# Types of Module in Python:


# 1. Built-in Modules: 
# pre-installed Modules in python.
# Examples include `math`, `os`, `sys`, etc.

# understand with code example:
import re 

# user_email = input("Enter your email: ")

# # Check if the entered email is valid using regular expression
# if re.match( r'^\S+@\S+\.\S+$', user_email): 
# # pattern is used to match perfect syntax of email :
# # ^  ->	Start of the string
# # \S+ ->	One or more non-space characters (used for the username part)
# # @  ->	The @ symbol literally
# # \S+ ->	One or more non-space characters again (for the domain part)
# # \. ->	A literal dot (. needs escaping because in regex it means any character)
# # \S+ ->	One or more non-space characters (for the domain extension like .com)
# #$	End of the string
#     print(" Your email is valid ✅ ") 
# else:
#     print("Your email is Invalid ❌")




# 2. User-defined Modules:

# Modules created by the user to organize their code.
# These can be created by simply saving Python code in a `.py` file.
# Example: `module_and_function.py`



#  3. External Modules (Third-party Libraries):
# Modules created by other developers and shared via the Python Package Index (PyPI).
# Examples include `requests`, `numpy`, `pandas`, etc.
# These can be installed using pip:
# pip install requests
# pip install numpy
# pip install pandas











# 2- Function in Python:
# A function is a block of reusable code that performs a specific task. They can take inputs (arguments) and return outputs.



# - Types of Python Functions:

# 1. Built-in Functions:
# Predefined functions in Python that perform specific tasks.
# Examples include `print()`, `len()`, `type()`, etc.

# print("HELLO! i'm khadijaaaa")
# print(len(user_email)) # print the length of the email


# 2. Functions defined in built-in modules:
import random

numbers: list[int] = [1,2,3,4,5,6,7,8,9,10]
print(random.choice(numbers)) # Randomly select an number from the list


# 3. User-defined Functions:
# Functions created by the user to perform specific tasks.

# a Simple Function :


def function_def():
    " This is a simple function definition"
    print("I'm a function!")
    return "This is the return value"

function_def() # Call the function to execute its code





# - Pass by Value Example (Immutable object):

#In this example, x remains unchanged after the modify function, because it's an immutable integer
def modify(x):
    " This function modifies a l by adding an element to it"
    x = 10
    print("Within Function " , x)

x = 5
print("original:", x)
modify(x) # Call the function to modify the variable
print("After Function " , x)


# - Pass by Reference Example (Mutable object):

#Now, let's use a dictionary (which is mutable) to demonstrate pass by reference.

def modify_dict(dict):
    " This function modifies a dictionary by adding an element to it"
    dict["name"] = "khadija"
    print("Inside Function " , dict)

new_dict = {"name": "ayesha"}
modify_dict(new_dict) # Call the function to modify the dictionary
print("outside Function " , new_dict)



# - Function Arguments:
#Function arguments are the values or variables passed into a function when it is called.

def user_info(name, age):
    " This function takes two arguments and prints them"
    print(f" hello I'm {name}, my age is {age} year old.")
    return 

user_info("khadija", 20) # Call the function to pass arguments
user_info("Ayesha", 18) # Call the function to pass arguments
user_info("haleema", 7) # Call the function to pass arguments



def dish_order(dish, size, ):
    " This function takes three arguments and prints them wih keyword "
    print(f"Dish: {dish}")
    print(f"Size: {size}")
    return

dish_order(dish="Pizza", size="Large") # Call the function to pass arguments with keyword
dish_order(dish="Burger", size="Medium") # Call the function to pass arguments with keyword
dish_order(dish="Pasta", size="Small") # Call the function to pass arguments with keyword



#- Unpacking Iterables with * in Python:

# The * operator can be used to unpack iterables (like lists or tuples) into function arguments. This allows you to pass multiple values to a function without explicitly listing them.

# Example of unpacking a list into function arguments:
def add_nums(a, b, c):
    return a + b + c
numbers_list = [1, 2, 3]
# Unpacking the list into separate arguments
result = add_nums(*numbers_list) #the list numbers = [1, 2, 3] is unpacked into separate arguments a, b, and c by using *numbers_list also function add nums then add these numbers together
print( "The result of ",result)





# - Default Arguments in Python
# Default arguments are values that are automatically assigned to function parameters if no value is provided when the function is called. This allows for more flexible function calls.


def profile_update(name, email, theme="Light"):
    print(f"Profile updated for {name} ({email})")
    print(f"Theme: {theme}")

# User who wants prefers a Dark theme
profile_update("Khadija", "khadija@gmail.com", theme="Dark")

# User who doesn't specify preferences, so defaults are used
profile_update("Ayesha", "ayesha@gmail.com")





# - Positional-only arguments:
#positional-only parameters in Python, introduced in Python 3.8.
# These parameters can only be passed positionally and cannot be used as keyword arguments. 
# The syntax for positional-only parameters is to use a slash (/) in the function definition. 
# -  Any parameters before the slash are positional-only, 
# -  while those after can be used as keyword arguments.

#understand by example:


def add(a, b, /,c):
    return a + b + c

print(add(1, 2, 3)) # positional arguments

# print(add(a=1, b=2, c=3)) # This will raise a TypeError because a and b are positional-only

print(add(1, 2, c=3)) # This will work because c can be passed as a keyword argument



# Keyword-only arguments:
# Keyword-only arguments are parameters that must be passed as keyword arguments.
# When you define a function with * in the parameter list, any parameters that come after the * must be passed using keyword syntax.


def food_order(dish, *, size, extra_toppings):
    print(f"Ordered {dish} in {size} size with {extra_toppings}")
    return

food_order("Pizza", size="Large", extra_toppings=["pepperoni", "mushrooms"]) # This works because size and extra_toppings are keyword-only arguments.

# food_order("Pizza", "Large", ["pepperoni", "mushrooms"]) # This will raise a TypeError because size and extra_toppings must be passed as keyword arguments



# - Arbitrary or Variable-length Arguments  or we also called (*args (Arbitrary Positional Arguments)):

# Arbitrary arguments allow you Collects extra positional arguments
# stored as tuple

# understand by coding example:
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
        print("The number is:", num)
    return total


addition = add_numbers(1, 2, 3, 4, 5)
print("The sum is:", addition) 

add_numbers(10, 20, 30) # Call the function with different number of arguments
 


# Arbitrary Keyword Arguments, (**kwargs):

#  Allow you toCollects extra keyword arguments.
# stored as dictionary

#understand by coding example:

def product_info(**details):
     " This function takes arbitrary keyword arguments and prints them"

     for key, value in details.items():
            print(f"{key}: {value}")


     print(details)
     return

product_info(name="Laptop", price=1000, brand="Dell") # Call the function with keyword arguments
new_product_info = {"name":"Phone", "price":"500$", "brand":"Samsung"} # Call the function with keyword arguments

product_info(**new_product_info) # Call the function with keyword arguments

# product_info(new_product_info) #see TypeError: product_info() takes 0 positional arguments but 1 was given

    


# - Python Function with Return Value
def calculate(a, b):
    result = a / b
    return result  # Return the sum of a and b

# Calling the function and storing the result
result = calculate(5, 2)

print("The sum is:", result)




# - Anonymous functions: (lambda Functions)
#The functions are called anonymous when they are not declared in the standard manner by using the def keyword. Instead, they are defined using the lambda keyword

# simple lambda function:

add = lambda x, y: x + y

result = add(5, 3)

print("The sum is:", result)



# - Scope of Variables:
#Scope refers to the region of the program where a variable is accessible. In Python, there are two main scopes:
# Global variables
# Local variables

#understand by example:
# Global variable
k = 10

def global_vs_local():
    "Accessing and modifying global variable inside the function"
    # Local variable
    y = 5
     
    global k
    k = 15  # Modifying global variable
    
    # Accessing local variable
    print("Infunction:")
    print("Global variable k:", k)
    print("Local variable y:", y)

# Calling the function
global_vs_local()

# Accessing global variable outside the function
print("Outside the function:")
print("Global variable k:", k)

# Uncommenting the following line will raise an error since y is a local variable
# print("Local variable y:", y)



# - Generator Function:

# A generator function is a special type of function in Python that:

# - Does not return all values at once

# -  Uses the yield keyword instead of return

# - Generates values one at a time, only when needed

# This makes it memory-efficient — especially when working with large amounts of data

# understand by code based example:
def reels_generator():
    "This function generates a sequence of numbers as reels using yield"
    for i in range(1, 10000):
        yield {f"reel_{i}"}

for reel in reels_generator():
    print(reel) # Prints each reel one at a time
    user = input("next reel? (y/n): ") #ask user for nexy real
    if user.lower() != "y" : # assume y as scroll down if user write y next number as reel appear
        break
    # Breaks the loop if user doesn't want to see next reel




# - generator expression:
# A generator expression is a concise way to create a generator without defining a separate function.
# genrator expression for squares of numbers from 0 to 4:
generator = (x * x for x in range(5))

# Using a generator: prints one-by-one, no memory taken upfront
for value in generator:
    # Prints each square one at a time
    # This doesn't store all the values at once but yields them one by one as you loop over them.
    print(value)



# - Recursive Function in Python:
#A recursive function is a function that calls itself to solve a smaller piece of the same problem… again and again… until it gets to the easiest version (called the base case), and then it stops

# - think of peeling onion layers:
#understand by code example:

def calculate_factr(n):
    # Base case
    if n == 0:
        return 1
    # Recursive case
    else:
        return n * calculate_factr(n - 1)

# Example usage
print(calculate_factr(6)) #output will be 720 

print(calculate_factr(5)) #output will be 120



# in the end, i wrotee to much comments to make understand every each step i use simple english word understand for every concept and trying make simple code example for every step hope this assignment is part 1 is completed and really enjoy to these concept.