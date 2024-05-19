import re

#Mini Project - Contact Management

def welcome_message():
    print("Welcome to your contacts!")
    print("Your contact options are listed below: ")
    print("Enter 1 to add a contact")
    print("Enter 2 to edit a contact")
    print("Enter 3 to search a contact")
    print("Enter 4 to display contact")
    print("Enter 5 to export contacts to a file")
    print("Enter 6 to import contacts from a file")
    print("Enter 7 to exit")


def add_contact(a, b, c, d):
    my_contacts["name"] = a
    my_contacts.update({"pnumber": b})
    my_contacts.update({"email address": c})
    my_contacts.update({"nature of contact": d})
    print(my_contacts)
    
    with open("contactman.txt", "w") as file:
        file.write(str(my_contacts))


def edit_contact(a, b, c, d):
    my_contacts.update({"name": a})
    my_contacts.update({"pnumber": b})
    my_contacts.update({"email address": c})
    my_contacts.update({"nature of contact": d})
    with open("contactman.txt", "w+") as file:  
        file.write(str(my_contacts))
    print(my_contacts)
                               

def search_contact(a, b):
    with open("contactman.txt", "r+") as file:
        """for i in file:
            if a in "name":
                contact = name[i]
                print(f"Name {contact} is in my contacts.")
            else:
                print(f"Name {i} is not in my contacts.")"""
        lines = file.read()
        for line in lines:
            for a, b in my_contacts.items():
                print(a, b)
                if a in line:
                    print(f"{a} {b} are in my contacts.")
                else:
                    print(f"{a}, {b} could not be found in the file.")



def display_contacts():
    with open("contactman.txt", "r") as file:
        for line in file:
            print(line)

def del_contacts():
    with open("contactman.txt", "r") as file:
        file.read()
        dkey = input("Enter key to be removed: ")
        #for a, b in my_contacts.items():
        #a, b = my_contacts.popitem()
        my_contacts.pop(dkey)
        print(my_contacts)
        #with open("contactman.txt", "a") as file:  
        #    file.write(str(my_contacts))



def exit_contacts():
    exit()

my_contacts = {}

welcome_message()

choice = int(input("Enter your choice from numbers 1 to 7: "))

if choice == 1:
    print("Adding contacts")
    lname = input("Enter last name: ")
    fname = input("Enter first name: ")
    name = lname + fname
    pnum = input("Enter phone number: ")
    eaddress = input("Enter email address, if any: ")
    porb = input("Enter relationship or professional link: ")
    add_contact(name, pnum, eaddress, porb)

if choice == 2:
    print("Editing contacts")
    lname = input("Enter last name: ")
    fname = input("Enter first name: ")
    name = lname + fname
    pnum = input("Enter phone number: ")
    eaddress = input("Enter email address, if any: ")
    porb = input("Enter relationship or professional link: ")
    edit_contact(name, pnum, eaddress, porb)

if choice == 3:
    skey = ""
    print("Search contacts")
    schoice = input("Enter a, b, c, or d for name, phone #, email or notes to be searched: ")
    if schoice == "a":
        skey = "name"
    if schoice == "b":
        skey = "pnumber"
    if schoice == "c":
        skey = "email address"
    if schoice == "d":
        skey = "nature of contact"
    svalue = input("Enter name of contact to search for: ")
    search_contact(skey, svalue)
    
if choice == 4:
    print("Displaying contacts")
    display_contacts()

if choice == 5:
    print("Deleting contacts")
    del_contacts() 




