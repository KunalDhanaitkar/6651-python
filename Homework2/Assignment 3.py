# Assignment 3 - Return the Shuffled String.
# Name: Kunal Dhanaitkar
# UNH ID: 00722835
# Major: Computer Science
# Course: 6651-02; Introduction to Script Programming/Python
# Submitted to: Professor Gulnora Nurmatova

# Using the typing package, to be able to specify a list of str's in a type hint.
from typing import List

# This class provides function which returns the shuffled string.
class Solution:

    # Defining function which takes a string and indices of the string as input and returns the shuffled string.
    def restoreString(self, s: str, indices: List[int]) -> str:

        # Variable to contain all the individual characters of a string in a list.
        t = list(s)
        # Counts the characters in the string.
        l = len(s)

        # For loop that iterates over all the characters of the string.
        for i in range(l):

            # Places all the characters of the string on their respective positions using indices.
            t[indices[i]] = s[i]

        # Joins all the shuffled characters together.
        return "".join(t)



