# Assignment 3 - Return the Shuffled String.
# Name: Kunal Dhanaitkar
# UNH ID: 00722835
# Major: Computer Science
# Course: 6651-02; Introduction to Script Programming/Python
# Submitted to: Professor Gulnora Nurmatova

# Declaring Variables
s="codeleet"
indices = [4,5,6,7,0,2,1,3]

# Variable to contain all the individual characters of a string in a list.
t = list(s)
# Counts the characters in the string.
l = len(s)

# For loop that iterates over all the characters of the string.
for i in range(l):

    # Places all the characters of the string on their respective positions using indices.
    t[indices[i]] = s[i]

    # Joins all the shuffled characters together and prints them out as output.
    print ("".join(t))



