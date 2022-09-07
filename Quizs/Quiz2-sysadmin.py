#Write a python script the user will enter a file name and you are required to read that 
#file and print the number of words in it.

#cat file2 | wc -w

#Answer
import subprocess

filename = input("Enter the file name: ")

mycommand1 = ["cat" , filename]
mycommand2 = ["wc" , "-w" , filename]

o1 = subprocess.Popen(mycommand1,stdout=subprocess.PIPE,universal_newlines=True)
o2 = subprocess.Popen(mycommand2,stdin=o1.stdout,stdout=subprocess.PIPE,universal_newlines=True).communicate()[0]

output = o1.communicate()[0]
print(type(output))
print(output)
print(o2)