# Assignment No 4
# part : 2
# topic :
# 1- Exception handling in python
# 2- NoReturn function


# -Exception handling in python
 # 1 - try Block 
# The try block is used to wrap code that might cause an error.
#understand by code :
try: 
    user = int(input("Enter a number: "))
    result = 10 / user
    print("Result is:", result)
except: # This block will execute if there is an exception in the try block like user input float or string and 0
    print("Error: You entered an invalid number like negative or 0  and string.")


# 2 - except Block:
# The except block handles the error that occurred in the try block. You can catch specific exceptions or use a general one.
#understand by code :
user_names = ["khadija", "zainab", "ayesha", "Aqsa"]
try:
    user_input = input("Enter your number between 0-3 to get a username : ")
    index = int(user_input)
    selected_username = user_names[index]

    print(f"entered name is: {selected_username.upper()}")
except ValueError :
    print("Error: Please enter a valid name." )
except IndexError:
    print("Error: Index out of range. Please enter a number between 0 and 3.")
except TypeError:
    print("Error: Please enter a valid number.")



# 3 - The else Block:
try:
    user = int(input("Enter a number: "))
    result = 10 / user
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("Result is:", result)



# 4 - The finally Block and raise Statement:
# The finally block is executed regardless of whether an exception occurred or not. It is often used for cleanup actions.
# The raise statement is used to raise your own exception manually.
#understand by code :

try:
    user = input("Enter your age : ")
    if not user.isdigit():
        # Check if the input is not a digit it raises a ValueError
        raise ValueError("Invalid age. Please enter a number.")
    age = int(user)
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print("Your age is:", age)
except ValueError as e:
    print("Error:", e)
finally:
    print("Execution completed.")
    #The finally block always runs, whether an exception occurs or not.


# - now we all exception with  single code example:

#understand by code :
def product_price_divider():
    try:
        price = input("Enter the total price of the products: ")
        totat_price = int(price)
        share_people = input("Enter the number of people to share the price: ")
        number_of_people = int(share_people)
       
        if not price.isdigit() or not share_people.isdigit():
            int("invalid")
        
            result = totat_price / number_of_people
    except ValueError :
        print("Error: Please enter a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed. Please enter a valid number of people.")
    else:
        print("Each person should pay:", result)
    finally:
        print("Thanks for Shopping.")



product_price_divider()

# - NoReturn function:
from typing import NoReturn

def exit_app() -> NoReturn:
    print("This function does not return anything.")
    raise SystemExit("Exiting the App. GoodBye")  # This will raise an exception and exit the program.

exit_app()

print("This line will NEVER run ❌")









