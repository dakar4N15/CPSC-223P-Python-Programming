import json
from datetime import datetime

class Appointments:
    def __init__(self, filename):
        self.filename = filename
        self.data = {}

        try:
            with open (self.filename, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            print(f"File '{self.filename}' not found. Created an empty data dictionary.")

    def add_appointment(self, phone, first, last, appt_datetime):
        if not phone.isdigit() or len(phone) != 10:
            return False
        
        if phone in self.data:
            return False
        
        try:
            datetime.strptime(appt_datetime, '%Y-%m-%d %H:%M')
        except ValueError:
            return False
        
        self.data[phone] = [first, last, appt_datetime]
        
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)
        
        return True
    
    def delete_appointment(self, phone):
        if not phone.isdigit() or len(phone) != 10:
            return False
        
        if phone not in self.data:
            return False
        
        del self.data[phone]

        with open(self.filename, 'w') as file:
            json.dump(self.data, file)
        
        return True
    
    def get_appointments(self, appt_date):
        try:
            datetime.strptime(appt_date, '%Y-%m-%d')
        except ValueError:
            return []
        
        result = []
        for phone, info in self.data.items():
            first, last, appt_datetime = info
            appt_dt = datetime.strptime(appt_datetime, '%Y-%m-%d %H:%M')
            
            if appt_dt.date() == datetime.strptime(appt_date, '%Y-%m-%d').date():
                result.append([
                    appt_dt.strftime('%B %d, %Y'),
                    appt_dt.strftime('%-I:%M %P'),
                    f"({phone[:3]}){phone[3:6]}-{phone[6:]}",
                    f"{first} {last}"
                ])

        return result