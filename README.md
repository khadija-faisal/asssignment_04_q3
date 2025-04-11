

# Assignment No 4 - Python

## Part 1: File Handling in Python

### File Handling Overview:
In Python, file handling is the process of creating, reading, writing, updating, and deleting files on your computer using Python.

### Functions:
- **open()**  
  Arguments:  
  - `file_name (str)` : The name of the file to be opened.  
  - `mode (str)` : The mode in which the file is to be opened (`r`, `w`, `a`, etc.).
  
- **write()**  
  Arguments:  
  - `text (str)` : The string to be written to the file.  

- **writelines()**  
  Arguments:  
  - `list (list)` : A list of strings to be written to the file.

- **read()**  
  Arguments:  
  - No arguments required.  
  Returns: A string containing all data from the file.

- **readline()**  
  Arguments:  
  - No arguments required.  
  Returns: A single line from the file.

- **seek()**  
  Arguments:  
  - `position (int)` : The position to which the file pointer should move.



---

## Part 2: Exception Handling in Python

### Exception Handling Overview:
Exception handling is a mechanism to handle runtime errors, ensuring that your program doesn't crash unexpectedly.

### Functions:
- **try**  
  No arguments, used to wrap code that may raise an error.
  
- **except**  
  Catches exceptions from the `try` block. It can catch specific exceptions or handle all with a general one.

- **else**  
  Executes if no exceptions occur in the `try` block.

- **finally**  
  Executes no matter what happens (exception or not), typically used for cleanup.

- **raise**  
  Arguments:  
  - `exception (Exception)` : The exception to be raised manually.



## Part 3: Date, Time, Calendar in Python and Math in Python

### Date and Time Overview:
Python provides modules like `time`, `datetime`, and `calendar` to work with date, time, and calendar-related tasks.

### Functions:
- **time.time()**  
  Arguments: None  
  Returns: Current time in seconds since the epoch (January 1, 1970).

- **time.localtime()**  
  Arguments:  
  - `seconds (float)` : The number of seconds since the epoch (use `time.time()`).
  Returns: A time-tuple with all valid time items.

- **datetime.datetime.now()**  
  Arguments: None  
  Returns: The current date and time.

- **datetime.datetime.strftime()**  
  Arguments:  
  - `format (str)` : Format string for the output date.
  Returns: Formatted string representing the date.

- **calendar.month()**  
  Arguments:  
  - `year (int)` : The year for the calendar.
  - `month (int)` : The month for the calendar.
  Returns: A string representing the month's calendar.

### Math Overview:
The `math` module provides various mathematical functions and constants.

### Functions:
- **math.sqrt()**  
  Arguments:  
  - `x (float)` : The number to find the square root of.
  Returns: The square root of `x`.

- **math.pow()**  
  Arguments:  
  - `x (float)` : The base number.
  - `y (float)` : The exponent.
  Returns: The result of `x` raised to the power of `y`.

- **math.factorial()**  
  Arguments:  
  - `n (int)` : The number for which to compute the factorial.
  Returns: The factorial of `n`.

- **math.ceil()**  
  Arguments:  
  - `x (float)` : The number to round up.
  Returns: The smallest integer greater than or equal to `x`.

- **math.pi**  
  No arguments  
  Returns: The value of π (approximately 3.14159).

- **math.log()**  
  Arguments:  
  - `x (float)` : The number to calculate the logarithm of.
  Returns: The natural logarithm of `x`.



---

Let me know if you need any further adjustments!
