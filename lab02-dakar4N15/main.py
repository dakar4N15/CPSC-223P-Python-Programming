# Name: William Sutanto
# Date: 2/2/2023
# File Purpose: Lab02 main program driver program

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
    print("5. Exit the program\n")
    
    #prompt the user for menu choice and call the appropriate contacts function or exit
    user_input = input("Enter menu choice: ")
    if(user_input == "1"):
        print_list(contacts)
    elif(user_input == "2"):
        add_contact(contacts)
    elif(user_input == "3"):
        modify_contact(contacts)
    elif(user_input == "4"):
        delete_contact(contacts)
    elif(user_input == "5"):
        exit = True
    else:
        print("Invalid choice!")
    
