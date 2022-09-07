#Reverse a given integer number

#Given:              76542

#Expected output:    24567

num = int(input("Type num: "))
revnum = 0
while (num > 0) :
    a = num % 10
    print(a)
    revnum = revnum * 10 + a
    num = num // 10
    
print(revnum)


#Another Answer
#num = input("Enter your Numbers: ")[::-1]
#print(num)