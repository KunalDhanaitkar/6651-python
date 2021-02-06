# Assignment 2 - Python program for "Guess the Number" game using Binary Search.
# Name: Kunal Dhanaitkar
# UNH ID: 00722835
# Major: Computer Science
# Course: 6651-02; Introduction to Script Programming/Python.
# Submitted to: Professor Gulnora Nurmotova

# Prompts the user to enter their name.
name = input('\nHi, What is your name?\n')
# Prints Hello and Introduces the game.
print('Hello ' + name + ', Let\'s play a Game.')
print('Think of random number from 1 to 100, and I\'ll try to guess it!')


# Defining function to calculate the number user guessed.
def guess_the_num():

    # Declaring variables to guess the number and also read the count number.
    count = 1
    l_num = 0
    h_num = 100
    mid = 50

    # Another loop which guesses the number the user thought of until found.
    while True:
        print("Is your number", mid, "? (Y/N)")
        user = input()

        # Condition to check if the guessed number is actual number.
        if user == "Y" or user == "y":
            print("Yeey! I Successfully Guessed your Number in ", count, " counts.")
            break

        # Condition to check if the guessed number is not correct.
        elif user == "N" or user == "n":
            print("Is the number greater than", mid, "? (Y/N)")
            user = input()

            # Condition to calculate if the number is greater than the middle number (Binary Search)
            if user == "Y" or user == "y":
                l_num = mid
                mid = round((h_num + mid) / 2)

            # Condition to calculate if the number is smaller than the middle number (Binary Search)
            elif user == "N" or user == "n":
                h_num = mid
                mid = round((l_num + mid) / 2)

            # Condition to check if the user has entered an input which is invalid.
            else:
                print("Invalid Input. Print 'Y'/'N'")

        # Condition to check if the user has entered an input which is invalid.
        else:
            print("Invalid Input. Print 'Y'/'N' ")

        # This counts how many times the loop has iterated.
        count += 1


# Calling function to guess the number.
guess_the_num()

while True:
    # Prompts the user if they want to play again.
    print("Do you want to play more? (Y/N)")
    user = input()

    # Condition to check if the user wants to play again.
    if user == "Y" or user == "y":
        # Calls the function again in order to play.
        guess_the_num()

    # Condition to check whether the user wants to exit out of the game.
    elif user == "N" or user == "n":
        print("Bye-Bye")
        break

    else:
        print("Invalid Input. Print 'Y'/'N' ")
