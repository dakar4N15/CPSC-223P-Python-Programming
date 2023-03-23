# Name: William Sutanto
# Date: 2/15/2023
# File Purpose: Lab04 main program driver program

from contacts import *

contacts = {}   #a variable to use for the contact list

exit = False    #loop controler

while(exit == False):
    #output menu choices
    print("\n      *** TUFFY TITAN CONTACT MAIN MENU\n")
    print("1. Add contact")
    print("2. Modify contact")
    print("3. Delete contact")
    print("4. Print contact list")
    print("5. Find contact")
    print("6. Exit the program\n")
    
    #prompt the user for menu choice and call the appropriate contacts function or exit
    user_input = input("Enter menu choice: ")
    if(user_input == "1"):
        phone = input("\nEnter phone number: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        value = add_contact(contacts, phone, first_name, last_name)
        if(value == "error"):
            print("Phone number already exists.")
        else:
            print("Added:", value[0], value[1],".")
    elif(user_input == "2"):
        phone = input("\nEnter phone number: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        value = modify_contact(contacts, phone, first_name, last_name)
        if(value == "error"):
            print("Phone number does not exist.")
        else:
            print("Modified:", value[0], value[1],".")
    elif(user_input == "3"):
        phone = input("\nEnter phone number: ")
        value = delete_contact(contacts, phone)
        if(value == "error"):
            print("Invalid phone number.")
        else:
            print("Deleted:", value[0], value[1],".")
    elif(user_input == "4"):
        print("\n==================== CONTACT LIST ====================")
        print("Last Name             First Name            Phone")
        print("====================  ====================  ==========")
        for key, names in contacts.items():
            print(f'{names[1]:22}{names[0]:22}{key:10}')
    elif(user_input == "5"):
        search = input("\nEnter search string: ")
        value = find_contact(contacts, search)
        print("\n================== FOUND CONTACT(S) ==================")
        print("Last Name             First Name            Phone")
        print("====================  ====================  ==========")
        for key, names in value.items():
            print(f'{names[1]:22}{names[0]:22}{key:10}')
    elif(user_input == "6"):
        exit = True
    else:
        print("Invalid choice!")

    
