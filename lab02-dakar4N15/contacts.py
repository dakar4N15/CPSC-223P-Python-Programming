# Name: William Sutanto
# Date: 2/2/2023
# File Purpose: Multiple contacts functions

def print_list(contacts):
    '''This function loops through the contact list
    and print each contact on a separate line displaying: 
    the list index number, the contact first name, and 
    the contact last name. '''

    print("\n================== CONTACT LIST ==================")
    print("Index   First Name            Last Name")
    print("======  ====================  ====================")
    for i in range(len(contacts)):
        print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')

def add_contact(contacts):
    '''This function adds a new contact to the list
    and return the updated list.'''

    first_name = input("\nEnter first name: ")
    last_name = input("Enter last name: ")
    new_contact = [first_name, last_name]
    contacts.append(new_contact)
    return contacts

def modify_contact(contacts):
    '''This function modify an existing contact in the
    contact list by changing the first and last name'''

    list_count = len(contacts)
    index =int(input("\nEnter the index number: "))
    if(index >= list_count):
        print("Invalid index number.")
        return contacts
    else:
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        new_contact = [first_name, last_name]
        contacts[index] = new_contact
        return contacts

def delete_contact(contacts):
    '''this function deletes a contact from the contact_list'''

    list_count = len(contacts)
    index = int(input("\nEnter the index number: "))
    if(index >= list_count):
        print("Invalid index number.")
        return contacts
    else:
        contacts.pop(index)
        return contacts


