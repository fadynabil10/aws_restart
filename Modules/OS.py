import os

l = ""

while l.upper() != "E" :
    l = input("type N to add new user or E for exit: ")
    if l.upper() == "N" :
        username = input("Please type username for new account: ")
        os.system(f"useradd {username}")
        os.system(f"passwd {username}")
        l = input("type N/E: ")
    
    elif l.upper() == "E" :
        print("Thank you")
    
    else :
        print("Type N or E: ")