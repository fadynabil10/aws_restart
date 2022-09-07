#Introducing System Administration with Python

#Using os.system

import os
import subprocess

os.system("ls")

#Using subprocess.run
subprocess.run(["ls"])

#Using subprocess.run with two arguments
subprocess.run(["ls","-l"])

#Using subprocess.run with three arguments
subprocess.run(["ls","-l","README.md"])

#Retrieving system information
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

#Retrieving information about disk space
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])