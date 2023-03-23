# Name: William Sutanto
# Date: 2/8/2023
# File Purpose: Lab03 main program driver program

from contacts import *

contacts = []   #a variable to use for the contact list

exit = False    #loop controler

while(exit == False):
    #output menu choices
    print("\n      *** TUFFY TITAN CONTACT MAIN MENU\n")
    print("1. Print list")
    print("2. Add contact")
    print("3. Modify contact")
    print("4. Delete contact")
    print("5. Sort list by first name")
    print("6. Sort list by last name")
    print("7. Exit the program\n")
    
    #prompt the user for menu choice and call the appropriate contacts function or exit
    user_input = input("Enter menu choice: ")
    if(user_input == "1"):
        print("\n================== CONTACT LIST ==================")
        print("Index   First Name            Last Name")
        print("======  ====================  ====================")
        for i in range(len(contacts)):
            print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')
    elif(user_input == "2"):
        first_name = input("\nEnter first name: ")
        last_name = input("Enter last name: ")
        add_contact(contacts, first_name, last_name)
    elif(user_input == "3"):
        index = int(input("\nEnter the index number: "))
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        return_value = modify_contact(contacts, first_name, last_name, index)
        if(return_value == False):
            print("Invalid index number.")
    elif(user_input == "4"):
        index = int(input("\nEnter the index number: "))
        return_value = delete_contact(contacts, index)
        if(return_value == False):
            print("Invalid index number.")
    elif(user_input == "5"):
        sort_contacts(contacts, column=0)
    elif(user_input == "6"):
        sort_contacts(contacts, column=1)
    elif(user_input == "7"):
        exit = True
    else:
        print("Invalid choice!")

    
