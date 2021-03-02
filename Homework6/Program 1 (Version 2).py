# Assignment 6 - (Program 1) - Program that takes a command line argument, search for a file in a directory indefinitely and display Alert if the file is deleted.
# Name: Kunal Dhanaitkar
# UNH ID: 00722835
# Major: Computer Science
# Course: 6651-02; Introduction to Script Programming/Python.
# Submitted to: Professor Gulnora Nurmotova


# import time module which gives us access to sleep function
import time

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


# run the loop indefinitely
while True:
    # get the current status i.e. True/False
    # True if file exists else False
    does_file_exist = os.path.exists(file_path)
    # check if file does not exist
    if does_file_exist == False:
        # if it does not exist
        # print Alert
        print('Alert')
        # exit the program
        sys.exit(0)

    # To reduce the load on CPU, sleep for 2 seconds after each iteration.
    time.sleep(2)