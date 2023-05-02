# Name: William Sutanto
# Date: 4/26/2023
# File Purpose: Lab10 contacts class

import sqlite3

class Contacts:
    db_name = ""
    
    #Declare a class variable to store the database file and intitialize it to an empty string.
    def __init__(self):
        self.db_name = ""
    
    def set_database_name(self, db_name):
        self.db_name = db_name
        
        # If the database file does not exist, create the contacts and phones tables
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS contacts
                     (contact_id INTEGER PRIMARY KEY,
                      first_name TEXT NOT NULL,
                      last_name TEXT NOT NULL)''')
        c.execute('''CREATE TABLE IF NOT EXISTS phones
                     (phone_id INTEGER PRIMARY KEY,
                      contact_id INTEGER NOT NULL,
                      phone_type TEXT NOT NULL,
                      phone_number TEXT NOT NULL,
                      FOREIGN KEY (contact_id) REFERENCES contacts(contact_id))''')
        conn.commit()
        conn.close()
        
    #return database name
    def get_database_name(self):
        return self.db_name
    
    #Insert new first name and last name into contacts table using SQL
    def add_contact(self, first_name, last_name):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("INSERT INTO contacts (first_name, last_name) VALUES (?, ?)", (first_name, last_name))
        conn.commit()
        conn.close()
        
    #Modify the first name and last name of the contact_id being passed using SQL UPDATE
    def modify_contact(self, contact_id, first_name, last_name):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("UPDATE contacts SET first_name=?, last_name=? WHERE contact_id=?", (first_name, last_name, contact_id))
        conn.commit()
        conn.close()
        
    #Insert contact_id, phone type, and phone number being passed into the phones table using SQL INSERT INTO
    def add_phone(self, contact_id, phone_type, phone_number):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("INSERT INTO phones (contact_id, phone_type, phone_number) VALUES (?, ?, ?)", (contact_id, phone_type, phone_number))
        conn.commit()
        conn.close()
    
    #Modify the phone type and phone number of the phone_id being passed using SQL UPDATE
    def modify_phone(self, phone_id, phone_type, phone_number):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("UPDATE phones SET phone_type=?, phone_number=? WHERE phone_id=?", (phone_type, phone_number, phone_id))
        conn.commit()
        conn.close()
        
    #Return an array that shows all contents of the database using SQL SELECT
    def get_contact_phone_list(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT contacts.*, phones.* FROM contacts LEFT JOIN phones ON contacts.contact_id=phones.contact_id")
        result = c.fetchall()
        conn.close()
        return result