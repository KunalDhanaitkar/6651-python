# Assignment 4 - (Program 1) - Python program to convert temperature from Fahrenheit to Celsius.
# Name: Kunal Dhanaitkar
# UNH ID: 00722835
# Major: Computer Science
# Course: 6651-02; Introduction to Script Programming/Python.
# Submitted to: Professor Gulnora Nurmotova


# Function to convert temperature Fahrenheit to Celsius.
def temp_c():
    # Prompts the user to enter temp in F°.
    fahrenheit = float(input("Enter temperature in fahrenheit(32° to 212°): "))

    # Condition to check whether the entered Fahrenheit is in valid range.
    if fahrenheit < 32 or fahrenheit > 212:
        print("Invalid input. Enter fahrenheit in range.")

    # If it is, Converts the F° to C° and prints it to the user.
    else:
        celsius = ((fahrenheit - 32) * 5.0 / 9.0)
        print('%.2f° Fahrenheit is: %0.2f° Celsius' % (fahrenheit, celsius))


# Calling the temperature converter function.
temp_c()

# Loop to prompt the user whether they want to convert the temperature again.
while True:
    print("Do you want to convert temperature F to C again? (Y/N)")
    user = input()

    # Condition to check if the user wants to convert again.
    if user == "Y" or user == "y":
        # Calls the temp converter function.
        temp_c()

    # Condition to check whether the user wants to exit out.
    elif user == "N" or user == "n":
        print("Bye-Bye")
        break

    else:
        print("Invalid Input. Print 'Y'/'N' ")