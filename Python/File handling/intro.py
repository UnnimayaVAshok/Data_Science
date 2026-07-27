# File Handling
#==================

# File is a collection of data stored permanently on a storage
# File handling is a technique with we can read,write,append and delete a file

# Type of modes in file handling

# read  "r"
# writr "w"
# append "a"
# delete

# Syntax
#==========

# open(filename/filepath,mode)

file = open("D:/Data_Science/Data_Science/Python/File handling/new.txt","r")

result = file.read()

print(result)

"""filename = input("Enter the file: ")

try:
    file = open(filename)

    result = file.read()

    print(result)

except FileNotFoundError:

    print("Enter the correct filename")

print("Thank you")
"""
# in "r" mode if the file doesnt exist it will raise an exception FileNotFound
#==================================================================================
"""
file = open("D:/Data_Science/Data_Science/Python/Basics/new_1.py","w")

file.write("# Helooooooooooooooo")

file.close()

# "w" mode used to write a file 

# in "w" mode if the filename is existing it overwrite all the content and write the given data

# if the file doesnt exist it will create a new file and write the content given

#================================================================================

file = open("D:/Data_Science/Data_Science/Python/Basics/new_1.py","a")


file.write(" Thank you")

file.close
"""

# using append mode it cannot overwrite the content in given file

# just append the content eith the existing data in the given file
"""
with open("new_1.py","w") as file:

    file.write("# Hai pythonn !!!")
"""
#  The file automatically closed with the block exists using with keyword

# readline() read a single line at a time

# readable() used to chack the file is able to read or not

# readlines() read all the lines and add each line as a element in list and return the list

file = open("new_1.py","r")

print(file.readlines())