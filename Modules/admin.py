#!/bin/python3
import os
import subprocess

def new_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Enter the name of the user to add: ")
        print("Use the username '" + username + "'? (Y/N)")
        confirm = input().upper()

    os.system(f"sudo useradd {username}") 


def remove_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Enter the name of the user to remove: ")
        print("Remove the user : '" + username + "'? (Y/N)")
        confirm = input().upper()
        
        os.system("sudo userdel -r " + username)

def add_user_to_group():
    username = input("Enter the name of the user that you want to add to a group: ")
    mycommand = ["cut","/etc/group","-d",":","-f","1"]
    output = subprocess.Popen(mycommand,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()[0]
    output = output.decode("utf-8")       # convert from byte to string
    grps = output.split("\n")
    print("Enter a list of groups to add the user to")
    print("The list should be separated by spaces, for example:\r\n group1 group2 group3")
    print("The available groups are:\r\n " + str(grps) )
    chosenGroups = input("Groups: ")
    chosenGroups = chosenGroups.split(" ")
    fla = True
    for c in chosenGroups: # 1 2 c
        for g in grps:        #a b c
            if g == c:
                fla = True
                break
            else:
                fla = False
        if fla == False:
            agcommand = ["sudo","groupadd",c]
            ag = subprocess.Popen(agcommand,stdout=subprocess.PIPE).communicate()[0]
        autgcommand = ["sudo","usermod",username,"-aG",c]
        autg = subprocess.Popen(autgcommand,stdout=subprocess.PIPE).communicate()[0]
#----------------------------------------------------------------------------------------
#Ahmad gamal idea

#    for c in chosenGroups:
#        if fla == True:           # 1 2 c
#            for g in grps:        #a b c
#                if g == c:
#                    fla = True
#                    break
#                else:
#                    fla = False
        
#        elif fla == False:
#            agcommand = ["sudo","groupadd",c]
#            ag = subprocess.Popen(agcommand,stdout=subprocess.PIPE).communicate()[0]

#        autgcommand = ["sudo","usermod",username,"-aG",c]
#        autg = subprocess.Popen(autgcommand,stdout=subprocess.PIPE).communicate()[0]





#new_user()
#remove_user()
add_user_to_group()



