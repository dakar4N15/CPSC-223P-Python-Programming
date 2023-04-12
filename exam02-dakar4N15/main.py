import appointments

a = appointments.Appointments('appointments.dat')

appts = a.get_appointments(appt_date='2023-09-12')

print("=============== APPOINTMENTS ================")
print()
print('Appointment Date: ' + appts[0][0])
print()
print('  Time       Phone              Name         ')
print('========  =============  ====================')
for x in appts:
    time = x[1]
    phone = x[2]
    name = x[3]
    print(f'{time:>8}  {phone:13}  {name:20}')

print()

'''
Expected output from the given appointments.dat file:

=============== APPOINTMENTS ================

Appointment Date: September 12, 2023

  Time       Phone              Name         
========  =============  ====================
 7:00 am  (585)757-4218  Lachlan Graves      
12:30 pm  (666)403-1404  Lillian Carson      
 4:15 pm  (738)705-9501  Karie Brandt        

'''

