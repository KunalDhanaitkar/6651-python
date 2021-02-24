# Assignment 5 - (Program 3) - Creating a Decorator Function that takes a function and prints the time it takes to execute it.
# Name: Kunal Dhanaitkar
# UNH ID: 00722835
# Major: Computer Science
# Course: 6651-02; Introduction to Script Programming/Python.
# Submitted to: Professor Gulnora Nurmotova

# Importing the Time module.
import time


def simple():  # Declaring a simple function.
    x = 4
    y = 4
    print(x*y)
    return 0


def decorate_it(simple):  # Decorator function.
    def newfunction():  # Creating the new function.
        a = 5
        b = 10
        print(a+b)
        simple()

    return newfunction  # Returning the new function.


start = time.time()
print("Test")
new_function = decorate_it(simple)
new_function()  # Calling the new function
end = time.time()
print("Time to execute the Function : ", end - start)
