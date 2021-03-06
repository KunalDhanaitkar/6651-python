# Assignment 6 - (Program 4) - Program to estimate how much operation on a dictionary is faster that operation on shelve.
# Name: Kunal Dhanaitkar
# UNH ID: 00722835
# Major: Computer Science
# Course: 6651-02; Introduction to Script Programming/Python.
# Submitted to: Professor Gulnora Nurmotova

# Importing the Time module.
import time

# Importing shelve module to store objects in a file.
import shelve


def shelfunc():  # Shelve Function
    db = shelve.open('C:/Users/kunal/test', 'c')
    db['bob'] = {'shoesize': 42, 'gender': 'm'}
    db['bob']
    {'shoesize': 42, 'gender': 'm'}
    db['bob']['gender'] = 'u'
    db['bob']
    {'shoesize': 42, 'gender': 'm'}
    db['bob'] = {'shoesize': 42, 'gender': 'u'}
    db['bob']
    {'shoesize': 42, 'gender': 'u'}


def dictfunc(): # Dictionary Function
    Dict = {1: 'My', 2: 'Name', 3: 'is', 4: 'Kunal'}
    # Deleting a key
    # using pop() method
    Dict.pop(4)


def decorate_it1(func):  # decorator function 1 for shelve
    def newfunction1():  # creating a new function
        print("\nOperation on a shelve: ")
        shelfunc()

    return newfunction1  # returning the new function


def decorate_it2(func):  # decorator function 2 for shelve
    def newfunction2():  # creating a new function
        print("\nOperation on a dictionary: ")
        dictfunc()

    return newfunction2  # returning the new function


print("\nHi, We\'ve used Decorator functions to estimate how much operation on a dictionary is faster than operation on shelve!")

start1 = time.time()
new_function = decorate_it1(shelfunc)
new_function()  # calling the new function with shelve
end1 = time.time()
print(end1 - start1)

start2 = time.time()
new_function1 = decorate_it2(dictfunc)
new_function1()  # calling the new function with dictionary
end2 = time.time()
print(end2 - start2)