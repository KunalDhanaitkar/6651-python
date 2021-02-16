# Assignment 4 - (Program 2) - Program to count how many times a word has appeared in a list and returns the count as a dictionary.
# Name: Kunal Dhanaitkar
# UNH ID: 00722835
# Major: Computer Science
# Course: 6651-02; Introduction to Script Programming/Python.
# Submitted to: Professor Gulnora Nurmotova

# Input List
mylist = ["one", "two", "eleven",  "one", "three", "two", "eleven", "three", "seven", "eleven"]


# Function to count the occurrence of a word in a list.
def count_frequency(mylist):
    count = dict()
    for word in mylist:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1

    return count


# Function call.
print(count_frequency(mylist))