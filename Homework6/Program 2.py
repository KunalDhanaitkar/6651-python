# Assignment 6 - (Program 2) - Modifying the quote generator program to create a new file for each quote from an Author.
# Name: Kunal Dhanaitkar
# UNH ID: 00722835
# Major: Computer Science
# Course: 6651-02; Introduction to Script Programming/Python.
# Submitted to: Professor Gulnora Nurmotova

import json, os
import shutil
import pathlib

PARENT_DIR = "quotes_output"

with open("quotes.json", 'r') as quotes_file:
    data = json.load(quotes_file)

# if the parent directory already there, we will delete it
if os.path.exists(PARENT_DIR):
    shutil.rmtree(PARENT_DIR)  # os.rmdir(PARENT_DIR)

os.mkdir(PARENT_DIR)  # parent directory
os.chdir(PARENT_DIR)  # change directory so that we are inside the parent directory
print("Created parent directory ", PARENT_DIR)

for node in data:
    flag = 1

count = 0
corrected_author = node["author"] if node["author"] is not None else "Unknown"
dir_name = corrected_author.replace(" ", "_")

if not os.path.exists(dir_name):
    os.mkdir(dir_name)

else:
    flag = 0
    print("{} already exists".format(dir_name))

os.chdir(dir_name)  # go inside the newly created directory

if flag == 0:
    for path in pathlib.Path(".").iterdir():
        if path.is_file():
            count += 1
            file_name = 'quote_' + str(count) + '.txt'
            out = open(file_name, "a+")
            out.write(node["text"])
            out.write("\n\n")
            out.close()
            os.chdir("..")  # go one level up in the directory tree

else:
    out = open("quote_1.txt", "a")
    out.write(node["text"])
    out.write("\n\n")
    out.close()
    os.chdir("..")
