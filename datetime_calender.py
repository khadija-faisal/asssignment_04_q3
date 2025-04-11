# Assignment No 4
# part : 4
# topic : 
# 1 - Date time and Calender in Python
# 2 - Math in Python



# What is Date, Time, and Calendar in Python?

#In Python, we use special modules (like tools) to work with date and time:
# Modules:
# 1. time: Works with the system time (in seconds).
# 2. datetime: Works with actual date and time (like 11 April 2025).
# 3. calendar: This module helps us work with calendars, like checking which day of the week a date falls on.


# - What is Epoch?
# Think of the epoch as “time zero” for computers.
# -  Epoch = January 1, 1970, 00:00:00 UTC
#  All computers including Python, start counting time from this point. 
import time

number_of_tick = time.time()  # Get the current time in seconds since the epoch
print("Number of seconds or tick since 12:00am, January 1, 1970:", number_of_tick)


#  - getting current time: (localtime())
current_locat_time = time.localtime(time.time())  # Get the current local time
print("Current local time:", current_locat_time) # that returns a time-tuple with all valid nine items.


#  - getting current formatted time: (asctime())
current_time = time.asctime(time.localtime(time.time()))
print(current_time)  # Convert the time tuple to a string

# the calender 
# The calendar module gives a wide range of methods to play with yearly and monthly calendars. 
import calendar
year = calendar.month(2024, 4)
print(year)  # Print the calendar for the year 2024
print("____________________")



#  - The datetime module:
import datetime
timing = datetime.datetime.now() #The date contains year, month, date, hour, minute, second, and microsecond.
print(timing)


# - The strftime() Method
# The strftime() method formats date objects into readable strings.

today = datetime.datetime(2025, 4, 12)

print(today.strftime("%f")) #Display Microsecond 000000-999999
print(today.strftime("%A")) #Display the name of the Day
print(today.strftime("%Y")) #Display the Year
print(today.strftime("%B")) #Display the name of the month

#another common formatting codes:
from datetime import datetime 
now = datetime.now()

print("Date and Time:", now.strftime("%A, %d %B %Y - %I:%M:%S:%f %p"))


#code   Meaning               :output example
# %A	Weekday name	       Saturday
# %d	Day (2 digits)	       12
# %B	Month name	           April
# %Y	Year (4 digits)	       2025
# %I	Hour (12-hour clock)   12
# %M	Minute (2 digits)	   56
# %S	Second (2 digits)	   33
# %f	Microsecond (6 digits) 889164
# %p	AM/PM	               AM


# - Python Math Module:
# The math module provides mathematical functions and constants.
import math

# - sqrt() function:
# The sqrt() function returns the square root of a number.
print("Square Root of 36:", math.sqrt(25))

# - pow() function:
# The pow() function returns the value of x raised to the power of y.
print("Power of 2^3:", math.pow(2, 3)) #2^3 = 8.0

# - pi constant:
# The pi constant represents the value of π (pi), approximately 3.14159.
print("Value of pi:", math.pi) #3.141592653589793

# - factorial() function:
# The factorial() function returns the factorial of a number.
print("Factorial of 5:", math.factorial(5)) #120

# - ceil() function:
# The ceil() function returns round up the float value.

print("Ceil of 4.3:", math.ceil(4.3)) #5

# round() function:
#  rounds a number to a specified number of decimal places
print("round(7.14159, 2) = ", round(7.14159, 2))  # outputs: 3.14

# max() Return:
# returns the largest of a set of numbers
print("max(5, 10, 15) = ", max(5, 10, 15))  # outputs: 15

# min() Return:
# returns the smallest of a set of numbers
print("min(5, 10, 15) = ", min(5, 10, 15))  # outputs: 5

# math.log() returns the natural logarithm of a number
print("math.log(7) = ", math.log(7))  # 
# outputs: 1.9459101490553132

# math.nan is a constant representing "not a number"
print("math.nan = ", math.nan)  # outputs: nan

# math.inf is a constant representing infinity
print("math.inf = ", math.inf)  # outputs: inf




