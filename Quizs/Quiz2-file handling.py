#Write a function in Python to count uppercase character in a text file.
#cat f1.txt
#I lOvE pyThon.

#Answer
def countf():
    file = open("f1.txt","r")
    data = file.read()
    print (data)
    count = 0
    for letter in data:
        if letter.isupper():
            count+=1
    print(count)
    file.close()

countf()