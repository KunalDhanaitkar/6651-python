# Assignment 6 - (Program 3) - Program that takes start path and name of a file, search for the file recursively and if found, display the full path of the file.
# Name: Kunal Dhanaitkar
# UNH ID: 00722835
# Major: Computer Science
# Course: 6651-02; Introduction to Script Programming/Python.
# Submitted to: Professor Gulnora Nurmotova

# import os module
# using os module, we can find if the file/directory exists.
import os

# Prompts the user for the path and the name of the file.
path = input("Enter the Path: ")
filename = input("Enter Filename: ")
full_path = []

# Finding path using os.walk method.
for root, dirs, files in os.walk(path):
    if filename in files:
        full_path.append(os.path.join(root, filename))

# Condition to display the output to the user.
if full_path == []:
    print("\nFile Not Found.")
else:
    print("\nFile Found.")
    print("Full Path of File is " + str(full_path[0]))