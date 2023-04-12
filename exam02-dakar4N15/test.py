import unittest
import io
import sys
import json
from unittest.mock import patch

import appointments

testfile = 'test99.dat'

import os
def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)

class Test01_AddAppointment_GoodDataSaved(unittest.TestCase):
    def test_list_int(self):
        remove_file(testfile)
        a = appointments.Appointments(testfile)
        a.add_appointment(phone='8006927753',first='Steve',last='Jobs', appt_datetime='2023-04-25 20:30')
        r = {}
        with open(testfile, 'r') as f:
            r = json.load(f)
        self.assertEqual(r, {"8006927753": ['Steve', 'Jobs', '2023-04-25 20:30']})
        remove_file(testfile)

class Test02_AddAppointment_GoodDataReturnedTrue(unittest.TestCase):
    def test_list_int(self):
        remove_file(testfile)
        a = appointments.Appointments(testfile)
        r = a.add_appointment(phone='8006927753',first='Steve',last='Jobs', appt_datetime='2023-04-25 20:30')
        self.assertEqual(r, True)
        remove_file(testfile)

class Test03_AddAppointment_BadPhoneTooShort(unittest.TestCase):
    def test_list_int(self):
        remove_file(testfile)
        a = appointments.Appointments(testfile)
        r = a.add_appointment(phone='6927753',first='Steve',last='Jobs', appt_datetime='2023-04-25 20:30')
        self.assertEqual(r, False)
        remove_file(testfile)

class Test04_AddAppointment_BadPhoneContainsAlphas(unittest.TestCase):
    def test_list_int(self):
        remove_file(testfile)
        a = appointments.Appointments(testfile)
        r = a.add_appointment(phone='aaa6927753',first='Steve',last='Jobs', appt_datetime='2023-04-25 20:30')
        self.assertEqual(r, False)
        remove_file(testfile)

class Test05_AddAppointment_BadPhoneAlreadyExists(unittest.TestCase):
    def test_list_int(self):
        remove_file(testfile)
        a = appointments.Appointments(testfile)
        r = a.add_appointment(phone='8006927753',first='Steve',last='Jobs', appt_datetime='2023-04-25 20:30')
        r = a.add_appointment(phone='8006927753',first='Steve',last='Jobs', appt_datetime='2023-04-25 20:30')
        self.assertEqual(r, False)
        remove_file(testfile)

class Test06_AddAppointment_BadDateTime(unittest.TestCase):
    def test_list_int(self):
        remove_file(testfile)
        a = appointments.Appointments(testfile)
        r = a.add_appointment(phone='8006927753',first='Steve',last='Jobs', appt_datetime='2023-04-32 20:30')
        self.assertEqual(r, False)
        remove_file(testfile)

class Test07_DeleteAppointment_GoodPhone(unittest.TestCase):
    def test_list_int(self):
        remove_file(testfile)
        a = appointments.Appointments(testfile)
        a.add_appointment(phone='8006927753',first='Steve',last='Jobs', appt_datetime='2023-04-25 20:30')
        a.delete_appointment(phone='8006927753')
        r = {}
        with open(testfile, 'r') as f:
            r = json.load(f)
        self.assertEqual(r, {})
        remove_file(testfile)

class Test08_DeleteAppointment_BadPhoneTooShort(unittest.TestCase):
    def test_list_int(self):
        remove_file(testfile)
        a = appointments.Appointments(testfile)
        a.add_appointment(phone='8006927753',first='Steve',last='Jobs', appt_datetime='2023-04-25 20:30')
        r = a.delete_appointment(phone='6927753')
        self.assertEqual(r, False)
        remove_file(testfile)

class Test09_DeleteAppointment_BadPhoneDoesNotExist(unittest.TestCase):
    def test_list_int(self):
        remove_file(testfile)
        a = appointments.Appointments(testfile)
        a.add_appointment(phone='8006927753',first='Steve',last='Jobs', appt_datetime='2023-04-25 20:30')
        r = a.delete_appointment(phone='8006927000')
        self.assertEqual(r, False)
        remove_file(testfile)

class Test10_GetAppointments_GoodDataFound(unittest.TestCase):
    def test_list_int(self):
        remove_file(testfile)
        a = appointments.Appointments(testfile)
        a.add_appointment(phone='8006927753',first='Steve',last='Jobs', appt_datetime='2023-04-25 08:30')
        a.add_appointment(phone='8006927753',first='Steve',last='Jobs', appt_datetime='2023-04-20 08:30')
        a.add_appointment(phone='8006427676',first='Bill',last='Gates',appt_datetime='2023-04-25 22:05')
        r = a.get_appointments(appt_date='2023-04-25')
        self.assertEqual(r, [['April 25, 2023','8:30 am','(800)692-7753','Steve Jobs'],['April 25, 2023','10:05 pm','(800)642-7676','Bill Gates']])
        remove_file(testfile)

class Test11_GetAppointments_GoodDataNotFound(unittest.TestCase):
    def test_list_int(self):
        remove_file(testfile)
        a = appointments.Appointments(testfile)
        a.add_appointment(phone='8006927753',first='Steve',last='Jobs', appt_datetime='2023-04-25 08:30')
        r = a.get_appointments(appt_date='2023-04-26')
        self.assertEqual(r, [])
        remove_file(testfile)

class Test12_GetAppointments_BadData(unittest.TestCase):
    def test_list_int(self):
        remove_file(testfile)
        a = appointments.Appointments(testfile)
        a.add_appointment(phone='8006927753',first='Steve',last='Jobs', appt_datetime='2023-04-25 08:30')
        r = a.get_appointments(appt_date='2023-04-35')
        self.assertEqual(r, [])
        remove_file(testfile)



if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
