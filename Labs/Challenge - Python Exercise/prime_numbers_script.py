#!/bin/python3
import subprocess

#lower = int(input("Enter lower number: "))
#upper = int(input("Enter upper number: "))

for num in range(1,250 + 1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)

with open("outfile.txt", "w+") as output:
    subprocess.call(["python", "./prime_numbers_script.py"], stdout=output);
