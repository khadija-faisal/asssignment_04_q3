# Assignment No 4
# part : 3
# topic : file handling in python



# -File handling in python:
#File handling lets you create, read, write, update, and delete files on your computer using Python.


# 1 - Opening a File:


# x: create mode. Opens the file for writing. Creates the file if it doesn't exist, or overwrites it if it does
demo_file = open("class.txt", "w")

# Mode	    Description
# 'r'	    Read (default)
# 'w'	    Write (overwrites file)
# 'a'	    Append (adds to file)
# 'x'	    Create new file
# 'b'	    Binary mode
# 't'	    Text mode (default)


#Writing to Files:

demo_file.write("Assalam- o -alaikum\n")  # \n creates a new line


# demo_file.write("this is khadija\n", "this is khadija\n" )  # This will raise an error because write() takes only one argument
demo_file.close()



# writelines(list): Writes a list of strings to the file.

fruits = ["apple\n", "banana\n", "cherry\n"]
demo_file = open("class.txt", "a")
# Open the file in append mode to add content  if we "w" it will overwrite the file deleting the previous content
demo_file.writelines(fruits)  # Append the list of fruits to the file
demo_file.close()


# Reading from Files:

demo_file = open("class.txt", "r") #open file in read mode

file_data = demo_file.read() 
print(file_data)  # Read the entire file content and print it

#like i want to read again one line of my demo_file but as the file pointer is at the end of the file so i have to use seek(0) to move the file pointer to the beginning of the file.

demo_file.seek(0)  # Move the file pointer to the beginning of the file

line = demo_file.readline()  # Read one line from the file
print(line)  # output : Assalam- o -alaikum



# using readlines to read all lines into a list

all_data = demo_file.readlines()  # Read all lines into a list
print(all_data) 

# Use "with " (best practice):
# Use with for automatic cleanup.
# Handle exceptions to avoid crashes.

try:
    with open("class.txt", "r") as demo_file:
        file_line = demo_file.readline()
        print(file_line)
except FileNotFoundError:
    print("File not found. Please check the file name and path.")






# create a example using all file handler methods dairy app:

try:
    with open("dairy.txt", "x") as file:
        file.write("This is my dairy.\n")
except FileExistsError:
        print("File already exists. Please choose a different name.")


user_entry = input("Enter today’s diary entry: ")
with open("dairy.txt", "a") as file:
    file.write(user_entry + "\n")  # Append the user entry to the file

print("Diary entry saved.\n")

print("Reading diary entries....\n")

with open("dairy.txt", "r") as file:
    content = file.read(40)
    print(content) 
    print("Current file pointer position:", file.tell())  # Print the current file pointer position
    file.seek(0)  # Move the file pointer to the beginning of the file

with open("dairy.txt", "r") as file:
    content = file.read()  # Read all lines into a list
    print(content)  # Print the list of lines

   































