# Name: William Sutanto
# Date: 3/22/2023
# File Purpose: Multiple contact functions

import json

class Contacts:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.data = {}
        
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            print(f"File '{self.filename}' not found. Created an empty contacts dictionary.")
    
    def add_contact(self, id, first_name, last_name):
        if id in self.data:
            return "error"
        
        self.data[id] = [first_name, last_name]
        self.data = dict(sorted(self.data.items(), key=lambda item: (item[1][1].lower(), item[1][0].lower())))
        
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)
        
        return self.data[id]

    def modify_contact(self, id, first_name, last_name):
        if id not in self.data:
            return "error"
        
        self.data[id] = [first_name, last_name]
        self.data = dict(sorted(self.data.items(), key=lambda item: (item[1][1].lower(), item[1][0].lower())))
        
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)
        
        return self.data[id]
    
    def delete_contact(self, id):
        if id not in self.data:
            return "error"
        
        deleted_contact = {id: self.data[id]}
        del self.data[id]
        
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)
        
        return deleted_contact
