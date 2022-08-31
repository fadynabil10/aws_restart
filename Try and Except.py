try :
    x=int(input("enter num: "))
    print (x/0)
except ZeroDivisionError:
    print ("Error, You cannot divide by 0!")
except ValueError :
    print ("Please enter an integer Number")
