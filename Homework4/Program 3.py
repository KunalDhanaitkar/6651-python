# Assignment 4 - (Program 3) LeetCode - Program to return indices of 2 numbers that add up to the target value.
# Name: Kunal Dhanaitkar
# UNH ID: 00722835
# Major: Computer Science
# Course: 6651-02; Introduction to Script Programming/Python.
# Submitted to: Professor Gulnora Nurmotova

# Declaring variables
nums = [8, 4, 7, 2, 5, 3, 5, 4, 5, 4, 5]
target = 6


# Defining function which returns indices of 2 numbers that add up to the target value.
def two_sum(nums, target):
    # Iterates over the list for the first value.
    for i in range(0, len(nums), 1):

        # Iterates over the list for the second value.
        for j in range(i + 1, len(nums), 1):

            # Condition to add up the two values one by one and compare it with the target value.
            if nums[i] + nums[j] == target:

                # Returns the indices of the two values that adds up to the target value..
                return i, j


# Calling function
print(two_sum(nums, target))