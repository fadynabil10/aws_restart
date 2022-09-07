#Write a function in python to count the number of lines from a text file "file1.txt" 
#which is not starting with an alphabet "t".

#cat file1.txt

#Answer
import os

def line_count():
    file = open("file1.txt","r")
    count=0
    for line in file:
        if line[0] not in 'T':
            count+= 1
    file.close()
    print("No of lines not starting with 'T'=",count)

line_count()
