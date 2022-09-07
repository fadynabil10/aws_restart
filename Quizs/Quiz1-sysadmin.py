# 1- Write ping python program where first ask the user for input,
# and then perform the ping request to that host.

#Answer

import subprocess

site = input("enter your site to ping: ")
n = input("number of times: ")

subprocess.run(['ping', site , "-c" , n])