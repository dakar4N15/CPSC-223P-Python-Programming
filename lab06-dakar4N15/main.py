# Name: William Sutanto
# Date: 3/15/2023
# File Purpose: Main file of lab06

import json
from weather import *

filename = "w.dat"
weather_dict = {}

exit = False    #loop controler

while(exit == False):
    #output menu choices
    print("\n      *** TUFFY TITAN WEATHER LOGGER MAIN MENU\n")
    print("1. Set data filename")
    print("2. Add weather data")
    print("3. Print daily report")
    print("4. Print historical report")
    print("9. Exit the program\n")
    
    #prompt the user for menu choice and call the appropriate contacts function or exit
    user_input = input("Enter menu choice: ")
    if(user_input == "1"):
        filename = input("Enter data filename: ")
        value = read_data(filename)
        weather_dict = value
    elif(user_input == "2"):
        date = input("\nEnter date (YYYYMMDD): ")
        time = input("Enter time (hhmmss): ")
        temperature = int(input("Enter temperature: "))
        humidity = int(input("Enter humidity: "))
        rainfall = float(input("Enter rainfall: "))
        date += time
        new_data = {date: {"t": temperature, "h": humidity, "r": rainfall}}
        weather_dict.update(new_data)
        write_data(weather_dict, filename)
    elif(user_input == "3"):
        date = input("\nEnter date (YYYYMMDD): ")
        string = report_daily(weather_dict, date)
        print(string)
    elif(user_input == "4"):
        string = report_historical(weather_dict)
        print(string)
        
    elif(user_input == "9"):
        exit = True
    else:
        print("Invalid choice!")