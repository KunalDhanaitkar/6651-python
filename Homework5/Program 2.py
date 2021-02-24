# Assignment 5 - (Program 2) - Recursive Function to return the number of "Ears" in a Bunny Line.
# Name: Kunal Dhanaitkar
# UNH ID: 00722835
# Major: Computer Science
# Course: 6651-02; Introduction to Script Programming/Python.
# Submitted to: Professor Gulnora Nurmotova

# Prompts user to enter no. of lines.
lines = int(input("Please enter the number of lines= "))


# Declaring a recursive function to calculate the no. of ears.
def ears(lines):

    # If true, exits out of the recursive function.
    if lines == 0:
        return 0

    # If remainder is 1, calls the recursive function until the number of lines is not 0 and adds 2 if the line is odd.
    elif lines % 2 == 1:
        return 2 + ears(lines - 1)

    # Adds 3 to the no of ears if the value of line is even.
    return 3 + ears(lines - 1)


# Prints the output.
print("\nThe Number of Ears in Bunny Line (", lines, ") = ", ears(lines))
