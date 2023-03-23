# Name: William Sutanto
# Date: 2/8/2023
# File Purpose: Multiple contacts functions

def add_contact(contacts, first_name, last_name):
    '''This function adds a new contact to the list
    and return the updated list.'''

    contacts.append([first_name, last_name])

def modify_contact(contacts, first_name, last_name, index):
    '''This function modify an existing contact in the
    contact list by changing the first and last name'''

    if(index >= len(contacts)):
        return False
    else:
        contacts[index] = [first_name, last_name]
        return True

def delete_contact(contacts, index):
    '''this function deletes a contact from the contact list'''

    if(index >= len(contacts)):
        return False
    else:
        contacts.pop(index)
        return True

def sort_contacts(contacts, column):
    '''this function sort the contacts in the contact list
        either by the first name or by the last name'''
    
    if(column == 0):
        sorted_contacts = sorted(contacts, key=lambda x: x[0])
        for i in range(len(contacts)):
            contacts[i] = [sorted_contacts[i][0], sorted_contacts[i][1]]
    elif(column == 1):
        sorted_contacts = sorted(contacts, key=lambda x: x[1])
        for i in range(len(contacts)):
            contacts[i] = [sorted_contacts[i][0], sorted_contacts[i][1]]

