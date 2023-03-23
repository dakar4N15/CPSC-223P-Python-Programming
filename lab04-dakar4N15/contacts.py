# Name: William Sutanto
# Date: 2/15/2023
# File Purpose: Multiple contacts functions

def add_contact(contacts, id, first_name, last_name):
    '''This function adds a new contact to the list
    and return the updated list.'''
    if id in contacts:
        return "error"
    else:
        contacts[id] = [first_name, last_name]
        return contacts[id]

def modify_contact(contacts, id, first_name, last_name):
    '''This function modify an existing contact in the
    contact list by changing the first and last name'''

    if id in contacts:
        contacts[id] = [first_name, last_name]
        return contacts[id]
    else:
        return "error"

def delete_contact(contacts, id):
    '''this function deletes a contact from the contact list'''

    if id in contacts:
        deleted = contacts[id]
        contacts.pop(id)
        return deleted
    else:
        return "error"

def sort_contacts(contacts):
    '''this function sort the dictionary in ascending order by 
    last name, and then by first name, ignoring case.'''

    sorted_contacts = dict(sorted(contacts.items(), key=lambda x: (x[1][1].lower(), x[1][0].lower())))
    contacts = sorted_contacts.copy()
    return contacts

def find_contact(contacts, find):
    '''this function will create an empty dictionary and will
    add the key:value pair to it if a key is found in the contacts
    dictionary, or if either a first or last name is found in contacts.
    find can be a numeric value that represents a key in the dictionary
    and can also be a substring that represents either first or last 
    name'''

    newdict = {}
    
    if find.isdigit():
        f = int(find)
        if f in contacts:
            newdict[f] = contacts[f]
    
    for key, names in contacts.items():
        if(find.lower() == names[0].lower() or find.lower() == names[1].lower()):
            newdict[key] = [names[0], names[1]]

    sort_contacts(newdict)
    return newdict



