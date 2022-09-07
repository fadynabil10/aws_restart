#Write a function in python to read the content from a text file "file1.txt" line by line and display the same on screen.

#cat file.txt

#Answer
import os

def read_file():
    file = open("file1.txt","r")
    for line in file:
        print(line, end="")
    file.close()

read_file()

#Another Answer

#with open("file1.txt") as file :
#    for line in (file.readlines()):
#        print(line)