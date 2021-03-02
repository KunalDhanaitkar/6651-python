# Assignment 6 - (Program 1) - Program that takes a command line argument, search for a file in a directory and Prints True/False if a file is available.
# Name: Kunal Dhanaitkar
# UNH ID: 00722835
# Major: Computer Science
# Course: 6651-02; Introduction to Script Programming/Python.
# Submitted to: Professor Gulnora Nurmotova

# import sys module
# it helps us to get the command line arguments
import sys

# import os module
# using os module, we can find if the file/directory exists
import os

# get the file path from arguments
# sys.argv is a list containing all the arguments passed
# the first element in the list is the file name itself
# so we take the element at index 1
file_path = sys.argv[1]

# check if file exists
# if the path exists, the following method return True else False
does_file_exist = os.path.exists(file_path)

# print True/False
print(does_file_exist)