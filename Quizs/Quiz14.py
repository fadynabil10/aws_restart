# Write a function named is_prime, which takes an integer as an argument and returns true 
# if the argument is a prime number, or false otherwise. Also, write function that generate random numbers 
# between 1 to 200 (the return value from this func is the argument for the is_prime func).

import random
def ran() :
    num = random.randint(1,200)
    return num

def is_prime (num) :
    print (num)
    for i in range(2,num) :
        if num % i == 0 :
            print ("The Number is Not Prime")
            break
        else :
            print ("The Number is Prime")
            break
        
is_prime(ran())    



# Second Solution

# Program to check if a number is prime or not
#num = 29

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
#flag = False

# prime numbers are greater than 1
#if num > 1:
#    # check for factors
#    for i in range(2, num):
#        if (num % i) == 0:
#            # if factor is found, set flag to True
#            flag = True
#            # break out of loop
#            break

# check if flag is True
#if flag:
#    print(num, "is not a prime number")
#else:
#    print(num, "is a prime number")