# Assignment 5 - (Program 1) - Using the generator function to create my own version of range function.
# Name: Kunal Dhanaitkar
# UNH ID: 00722835
# Major: Computer Science
# Course: 6651-02; Introduction to Script Programming/Python.
# Submitted to: Professor Gulnora Nurmotova

# Declaring function which will provide a resemblance to the range() function.
def my_range(start, stop, step=1):
    num_list = []
    # Loop to traverse through the parameters in the range and adds the values to the list created..
    while start < stop:
        num_list.append(start)
        start += step
    return num_list

# Calling the my_range function instead of the pre-defined range() function in python.
for i in my_range(0, 10, 2):
    print(i)
