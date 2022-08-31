#type python function to generate random odd numbers.

#hint: use random library


#Random Odd Number Function
import random

#Method #2: Using an algorithm based on iteration
def randomOddNumber(a,b):
  number = random.randint(a,b)
  while number % 2 == 0:
    number = random.randint(a,b)
  
  return number
  
oddNumber = randomOddNumber(0,100) 
print(oddNumber)